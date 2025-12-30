import time
import math
import rclpy
from rclpy.action import ActionServer, GoalResponse
from rclpy.node import Node
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.executors import MultiThreadedExecutor

from turtle_control_action.action import Navigate
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist


class TurtleControlServer(Node):

    def __init__(self):
    
        super().__init__('turtle_control_server')
        
        # Usar callback group reentrante para permitir processamento concorrente
        self.callback_group = ReentrantCallbackGroup()
        
        # Inicializar variáveis
        self.current_x = 0.0
        self.current_y = 0.0
        self.current_theta = 0.0
        self.has_pose = False
        
        # Parâmetros do controle
        self.k_omega = 2.5     # Ganho para velocidade angular
        self.v_max = 2.0       # Velocidade linear máxima
        self.threshold = 0.05  # Limiar de convergência (metros)
        self.v_lim = 3.0       # Limite de velocidade linear
        self.w_lim = 3.0       # Limite de velocidade angular
        
        # Subscriber para pose da tartaruga
        self.pose_subscriber = self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10, callback_group=self.callback_group)
        
        # Publisher para velocidade
        self.cmd_vel_publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        
        # Action server
        self._action_server = ActionServer(
            self,
            Navigate,
            'navigate',
            self.execute_callback,
            goal_callback=self.goal_callback,
            handle_accepted_callback=self.handle_accepted_callback,
            cancel_callback=self.cancel_callback,
            callback_group=self.callback_group
        )
        
        self.get_logger().info('Turtle Control Server inicializado!')
    
    def pose_callback(self, msg):
    
        """Callback para receber a pose atual da tartaruga"""
        
        self.current_x = msg.x
        self.current_y = msg.y
        self.current_theta = msg.theta
        self.has_pose = True
    
    def goal_callback(self, goal_request):
    
        """Callback quando um novo goal é recebido"""
        
        self.get_logger().info(f'Novo goal recebido: ({goal_request.goal_x:.2f}, {goal_request.goal_y:.2f})')
        
        if not self.has_pose:
            self.get_logger().warn('Pose da tartaruga ainda não recebida!')
            return GoalResponse.REJECT
        
        # Verificar se o goal está dentro dos limites do turtlesim (0-11)
        if (goal_request.goal_x < 0 or goal_request.goal_x > 11 or goal_request.goal_y < 0 or goal_request.goal_y > 11):
            self.get_logger().warn(f'Goal fora dos limites: ({goal_request.goal_x:.2f}, {goal_request.goal_y:.2f})')
            return GoalResponse.REJECT
        
        return GoalResponse.ACCEPT
    
    def handle_accepted_callback(self, goal_handle):
    
        """Callback quando um goal é aceito"""
        
        self.get_logger().info('Goal aceito, executando...')
        goal_handle.execute()
    
    def cancel_callback(self, goal_handle):
    
        """Callback quando uma ação é cancelada"""
        
        self.get_logger().info('Goal cancelado!')
        
        # Publicar velocidade zero para parar a tartaruga
        stop_msg = Twist()
        self.cmd_vel_publisher.publish(stop_msg)
        
        return True  # Aceita o cancelamento
    
    def calculate_control(self, goal_x, goal_y):
    
        """Calcula os comandos de controle baseados na pose atual e objetivo"""
        
        # Calcular erros
        x_error = goal_x - self.current_x
        y_error = goal_y - self.current_y
        
        # Coordenadas polares
        rho = math.sqrt(x_error**2 + y_error**2)  # Distância
        alpha = math.atan2(y_error, x_error) - self.current_theta  # Ângulo
        alpha = math.atan2(math.sin(alpha), math.cos(alpha))  # Normalizar
        
        # Lei de controle
        if rho > self.threshold:
            v = self.v_max * math.tanh(rho)
            w = self.k_omega * alpha
            
            # Limitar velocidades
            v = max(-self.v_lim, min(self.v_lim, v))
            w = max(-self.w_lim, min(self.w_lim, w))
        else:
            # Objetivo alcançado
            v = 0.0
            w = 0.0
        
        return v, w, rho
    
    def execute_callback(self, goal_handle):
    
        """Callback principal de execução da ação"""
        
        self.get_logger().info('Executando goal...')
        
        # Obter objetivo da requisição
        goal_x = goal_handle.request.goal_x
        goal_y = goal_handle.request.goal_y
        
        feedback_msg = Navigate.Feedback()
        result = Navigate.Result()
        
        # Taxa de controle (10 Hz)
        control_rate = self.create_rate(10, self.get_clock())
        
        try:
            # Loop de controle até alcançar o objetivo
            while rclpy.ok():
                # Verificar se o goal foi cancelado
                if goal_handle.is_cancel_requested:
                    goal_handle.canceled()
                    self.get_logger().info('Goal cancelado durante execução')
                    
                    # Publicar velocidade zero
                    stop_msg = Twist()
                    self.cmd_vel_publisher.publish(stop_msg)
                    
                    result.success = False
                    result.current_x = self.current_x
                    result.current_y = self.current_y
                    return result
                
                # Calcular controle
                v, w, distance = self.calculate_control(goal_x, goal_y)
                
                # Publicar feedback
                feedback_msg.current_x = self.current_x
                feedback_msg.current_y = self.current_y
                feedback_msg.distance_to_goal = distance
                goal_handle.publish_feedback(feedback_msg)
                
                # Publicar comando de velocidade
                cmd_vel_msg = Twist()
                cmd_vel_msg.linear.x = float(v)
                cmd_vel_msg.angular.z = float(w)
                self.cmd_vel_publisher.publish(cmd_vel_msg)
                
                self.get_logger().debug(
                    f'Pose: ({self.current_x:.2f}, {self.current_y:.2f}) | '
                    f'Goal: ({goal_x:.2f}, {goal_y:.2f}) | '
                    f'Dist: {distance:.2f} | '
                    f'Vel: ({v:.2f}, {w:.2f})'
                )
                
                # Verificar se objetivo foi alcançado
                if distance < self.threshold:
                    self.get_logger().info('Goal alcançado!')
                    
                    # Publicar velocidade zero final
                    stop_msg = Twist()
                    self.cmd_vel_publisher.publish(stop_msg)
                    
                    # Definir resultado
                    goal_handle.succeed()
                    result.success = True
                    result.current_x = self.current_x
                    result.current_y = self.current_y
                    return result
                
                control_rate.sleep()
        
        except Exception as e:
            self.get_logger().error(f'Erro durante execução: {str(e)}')
            
            # Publicar velocidade zero em caso de erro
            stop_msg = Twist()
            self.cmd_vel_publisher.publish(stop_msg)
            
            result.success = False
            result.current_x = self.current_x
            result.current_y = self.current_y
            return result
    
    def destroy_node(self):
    
        """Override do destroy_node para parar a tartaruga antes de destruir"""
        
        # Publicar velocidade zero antes de terminar
        stop_msg = Twist()
        self.cmd_vel_publisher.publish(stop_msg)
        super().destroy_node()


def main(args=None):

    rclpy.init(args=args)
    
    try:
        # Criar servidor
        turtle_control_server = TurtleControlServer()
        
        # Usar executor multi-threaded para lidar com callbacks concorrentes
        executor = MultiThreadedExecutor()
        executor.add_node(turtle_control_server)
        
        executor.spin()
        
    except KeyboardInterrupt:
        turtle_control_server.get_logger().info('Servidor interrompido pelo usuário')
    finally:
        # Garantir que a tartaruga pare
        if 'turtle_control_server' in locals():
            turtle_control_server.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
