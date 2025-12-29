"""
Nó de controle para Turtlesim
Subscreve: /turtle1/pose e /goal
Publica: /turtle1/cmd_vel
Controla a tartaruga para posição objetivo usando controle proporcional
"""

import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Pose2D, Twist
import math


class TurtleControl(Node):

    def __init__(self):
    
        super().__init__('turtle_control')
        
        # Inicializa variáveis primeiro
        self.init_variables()
        
        # Inicializa publisher e subscribers
        self.init_publisher()
        self.init_subscribers()
        
        self.get_logger().info('Nó de controle inicializado! Aguardando pose e goal...')
    
    def init_variables(self):
    
        """Inicializa todas as variáveis do controle"""
        
        # Pose atual da tartaruga
        self.current_x = 0.0
        self.current_y = 0.0
        self.current_theta = 0.0
        
        # Posição objetivo
        self.goal_x = 0.0
        self.goal_y = 0.0
        
        # Erros
        self.x_error = 0.0
        self.y_error = 0.0
        self.rho = 0.0      # Distância em coordenadas polares
        self.alpha = 0.0    # Ângulo em coordenadas polares
        
        # Parâmetros do controle
        self.k_omega = 2.5     # Ganho para velocidade angular
        self.v_max = 2.0       # Velocidade linear máxima
        self.threshold = 0.05  # Limiar de convergência (metros)
        self.v_lim = 3.0       # Limite de velocidade linear
        self.w_lim = 3.0       # Limite de velocidade angular
        
        # Flags de recebimento
        self.has_pose = False
        self.has_goal = False
        self.has_achieved = False
        
        self.get_logger().info('Variáveis inicializadas')
    
    def init_publisher(self):
    
        """Inicializa o publisher de velocidade"""
        
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        
        # Timer para publicar velocidade a cada 0.1 segundos
        timer_period = 0.1  # segundos
        self.timer = self.create_timer(timer_period, self.pub_callback)
        
        self.get_logger().info('Publisher de cmd_vel inicializado')
    
    def init_subscribers(self):
    
        """Inicializa os subscribers"""
        
        # Subscriber para pose da tartaruga
        self.pose_subscriber = self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)
        
        # Subscriber para posição objetivo
        self.goal_subscriber = self.create_subscription(Pose2D, '/goal', self.goal_callback, 10)
        
        self.get_logger().info('Subscribers inicializados')
    
    def pose_callback(self, msg):
    
        """Callback para receber a pose da tartaruga"""
        
        self.current_x = msg.x
        self.current_y = msg.y
        self.current_theta = msg.theta
        
        # Marca que recebeu pose
        if not self.has_pose:
            self.has_pose = True
            self.get_logger().info(f'Pose inicial recebida: x={msg.x:.2f}, y={msg.y:.2f}, theta={msg.theta:.2f}')
        
        # Calcular erros se já tem goal
        if self.has_goal:
            self.calculate_errors()
    
    def goal_callback(self, msg):
    
        """Callback para receber posição objetivo"""
        
        self.goal_x = msg.x
        self.goal_y = msg.y
        
        if not self.has_goal:
            self.has_goal = True
            self.get_logger().info(f'Goal recebido: x={msg.x:.2f}, y={msg.y:.2f}')
        else:
            self.get_logger().info(f'Novo goal: x={msg.x:.2f}, y={msg.y:.2f}')
        
        # Calcular erros se já tem pose
        if self.has_pose:
            self.calculate_errors()
    
    def calculate_errors(self):
    
        """Calcula erros em coordenadas cartesianas e polares"""
        
        # Erros em coordenadas cartesianas
        self.x_error = self.goal_x - self.current_x
        self.y_error = self.goal_y - self.current_y
        
        # Coordenadas polares
        self.rho = math.sqrt(self.x_error**2 + self.y_error**2)  # Distância
        self.alpha = math.atan2(self.y_error, self.x_error) - self.current_theta  # Ângulo
        self.alpha = math.atan2(math.sin(self.alpha), math.cos(self.alpha))       # Normalizar
        
        # Log para debugging
        self.get_logger().debug(
            f'Erros: x={self.x_error:.2f}, y={self.y_error:.2f}, '
            f'rho={self.rho:.2f}, alpha={self.alpha:.2f}'
        )
    
    def pub_callback(self):
    
        """
        Callback principal do timer
        Calcula controle e publica velocidade
        """
        
        # Só publica se já recebeu pose e goal
        if not (self.has_pose and self.has_goal):
            return
        
        # Calcula controle se necessário
        if self.rho > self.threshold:
            # Lei de controle
            v = self.v_max * math.tanh(self.rho)
            w = self.k_omega * self.alpha
            
            # Limita velocidades
            v = max(-self.v_lim, min(self.v_lim, v))  # Limite de velocidade linear
            w = max(-self.w_lim, min(self.w_lim, w))  # Limite de velocidade angular
            
            self.has_achieved = False
        else:
            # Já está no objetivo (dentro do limiar)
            v = 0.0
            w = 0.0
            self.has_achieved = True
        
        # Cria mensagem de velocidade
        cmd_vel_msg = Twist()
        cmd_vel_msg.linear.x = float(v)
        cmd_vel_msg.angular.z = float(w)
        
        # Publica
        self.publisher_.publish(cmd_vel_msg)
        
        # Log para monitoramento
        self.get_logger().debug(f'Publicando: v={v:.2f}, w={w:.2f}')
        
        # Log periódico
        if hasattr(self, 'counter'):
            self.counter += 1
            if self.counter % 10 == 0:  # A cada 1 segundo (0.1s * 10)
	            self.get_logger().info(
	                f'Pose: ({self.current_x:.1f}, {self.current_y:.1f}) | '
	                f'Goal: ({self.goal_x:.1f}, {self.goal_y:.1f}) | '
	                f'Dist: {self.rho:.2f}'
	            )
	            if self.has_achieved:
	            	self.get_logger().info('Objetivo alcançado!')
        else:
            self.counter = 0


def main(args=None):

    rclpy.init(args=args)
    
    # Cria nó
    turtle_control = TurtleControl()
    
    try:
        # Mantém nó rodando
        rclpy.spin(turtle_control)
    except KeyboardInterrupt:
        turtle_control.get_logger().info('Controle interrompido pelo usuário')
    finally:
        # Publica velocidade zero antes de terminar
        stop_msg = Twist()
        turtle_control.publisher_.publish(stop_msg)
        
        # Destrói nó
        turtle_control.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
