"""
Nó Waypoint Manager - Publica goals sequenciais quando robô chega no anterior
Monitora pose do robô e só publica próximo goal quando alcança o atual
"""

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose2D
from turtlesim.msg import Pose
import math


class WaypointManager(Node):

    def __init__(self):
    
        super().__init__('waypoint_manager')
        
        # Publisher para enviar goals ao controlador
        self.goal_publisher = self.create_publisher(Pose2D, '/goal', 10)
        
        # Subscriber para monitorar pose do robô
        self.pose_subscriber = self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)
        
        # Array de waypoints (posições objetivo)
        self.waypoints = [
            (5.0, 5.0, 0.0),    # Centro
            (1.0, 1.0, 0.0),    # Canto inferior esquerdo
            (9.0, 1.0, 0.0),    # Canto inferior direito
            (9.0, 9.0, 0.0),    # Canto superior direito
            (1.0, 9.0, 0.0),    # Canto superior esquerdo
            (5.0, 5.0, 0.0),    # Volta ao centro
        ]
        
        # Estado atual
        self.current_waypoint_index = 0
        self.current_goal = None
        self.robot_pose = None
        self.delay_timer = None
        self.goal_reached = False
        self.distance_threshold = 0.05  # Metros de tolerância
        
        # Publica primeiro goal imediatamente
        self.publish_next_waypoint()
        
        self.get_logger().info('Waypoint Manager inicializado!')
        self.get_logger().info(f'Total de {len(self.waypoints)} waypoints configurados')
    
    def pose_callback(self, msg):
    
        """Recebe a pose atual do robô e verifica se chegou ao goal"""
        
        self.robot_pose = msg
        
        if self.current_goal is not None and self.robot_pose is not None:
        
            # Calcula distância até goal atual
            dx = self.current_goal.x - self.robot_pose.x
            dy = self.current_goal.y - self.robot_pose.y
            distance = math.sqrt(dx**2 + dy**2)
            
            # Verifica se chegou
            if distance < self.distance_threshold and not self.goal_reached:
                self.goal_reached = True
                self.get_logger().info(f'Waypoint {self.current_waypoint_index} alcançado!')
                self.get_logger().info(f'Posição: ({self.robot_pose.x:.2f}, {self.robot_pose.y:.2f})')
                
                # Pequeno delay antes de publicar próximo
                self.schedule_next_waypoint(1.0)

    def schedule_next_waypoint(self, delay):
	
        """Agenda o próximo waypoint da lista com o temporizador"""
	
        if self.delay_timer is not None:
            return  # já existe um timer ativo

        self.delay_timer = self.create_timer(delay, self.publish_next_waypoint_delayed)

    def publish_next_waypoint_delayed(self, timer=None):
    
        """Callback do timer delay para publicar próximo waypoint"""
        
        if self.delay_timer is not None:
        	self.delay_timer.destroy()
        	self.delay_timer = None

        self.publish_next_waypoint()
    
    def publish_next_waypoint(self):
    
        """Publica próximo waypoint da lista"""
        
        if self.current_waypoint_index < len(self.waypoints):
        
            # Pega próximo waypoint
            x, y, theta = self.waypoints[self.current_waypoint_index]
            
            # Cria mensagem
            self.current_goal = Pose2D()
            self.current_goal.x = float(x)
            self.current_goal.y = float(y)
            self.current_goal.theta = float(theta)
            
            # Publica
            self.goal_publisher.publish(self.current_goal)
            
            self.get_logger().info(f'Publicando waypoint {self.current_waypoint_index}: ({x:.1f}, {y:.1f}, θ={theta:.1f})')
            
            # Prepara para próximo
            self.current_waypoint_index += 1
            self.goal_reached = False
            
        else:
        
            self.get_logger().info('Todos waypoints completados!')
            self.get_logger().info('Reiniciando sequência...')
            
            # Reinicia sequência
            self.current_waypoint_index = 0
            self.schedule_next_waypoint(3.0)

def main(args=None):

    rclpy.init(args=args)
    
    waypoint_manager = WaypointManager()
    
    try:
        rclpy.spin(waypoint_manager)
    except KeyboardInterrupt:
        waypoint_manager.get_logger().info('Waypoint Manager interrompido')
    finally:
        waypoint_manager.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
