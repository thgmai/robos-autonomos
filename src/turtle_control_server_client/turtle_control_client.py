import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node
import yaml
import os
import math
import sys
import shutil

from turtle_control_action.action import Navigate


class TurtleControlClient(Node):

    def __init__(self):

        super().__init__('turtle_control_client')
        
        self._action_client = ActionClient(self, Navigate, 'navigate')
        
        # Variáveis de estado
        self.waypoints = []
        self.current_waypoint_index = 0
        self.is_executing = False
        self.delay_timer = None
        self.distance_threshold = 0.05  # 5 cm de tolerância
        
        # Carregar waypoints do arquivo YAML
        self.load_waypoints()
        
        self.get_logger().info('Turtle Control Client inicializado!')
        self.get_logger().info(f'Carregados {len(self.waypoints)} waypoints')
        
        # Timer para iniciar a sequência após inicialização
        self.schedule_next_waypoint(1.0)
    
    def load_waypoints(self):
    
        """Carrega waypoints de um arquivo YAML"""
        
        try:
        
            path = 'src/turtle_control_server_client/waypoints.yaml'
            
            if not os.path.exists(path):
                self.get_logger().error('Arquivo waypoints.yaml não encontrado.')
                self.destroy_node()
                return
            
            with open(path, 'r') as file:
            
                config = yaml.safe_load(file)
                
                if 'waypoints' in config:
                    self.waypoints = config['waypoints']
                    # Garantir que cada waypoint tenha exatamente 2 valores (x, y)
                    validated_waypoints = []
                    for wp in self.waypoints:
                        if isinstance(wp, list) and len(wp) == 2:
                            validated_waypoints.append((float(wp[0]), float(wp[1])))
                        else:
                            self.get_logger().warn(f'Waypoint inválido ignorado: {wp}')
                    self.waypoints = validated_waypoints
                    self.get_logger().info(f'Waypoints carregados: {self.waypoints}')
                else:
                    self.get_logger().error('Formato inválido: arquivo deve conter chave "waypoints"')
                    self.destroy_node()
                    
        except yaml.YAMLError as e:
            self.get_logger().error(f'Erro ao parsear YAML: {e}')
            self.destroy_node()
        except Exception as e:
            self.get_logger().error(f'Erro ao carregar waypoints: {e}')
            self.destroy_node()
    
    def start_sequence(self):
    
        """Inicia a sequência de waypoints"""
        
        if not self.is_executing and len(self.waypoints) > 0:
            self.send_next_waypoint()
    
    def send_next_waypoint(self):
    
        """Envia o próximo waypoint da lista"""
        
        if self.current_waypoint_index >= len(self.waypoints):
            self.get_logger().info('Todos os waypoints foram completados!')
            self.get_logger().info('Reiniciando sequência...')
            self.current_waypoint_index = 0
            
            # Aguarda 3 segundos antes de reiniciar
            self.schedule_next_waypoint(3.0)
            return
        
        # Pega o próximo waypoint
        goal_x, goal_y = self.waypoints[self.current_waypoint_index]
        
        # Cria a mensagem de goal
        goal_msg = Navigate.Goal()
        goal_msg.goal_x = float(goal_x)
        goal_msg.goal_y = float(goal_y)
        
        self.get_logger().info(f'Enviando waypoint {self.current_waypoint_index}: ({goal_x:.1f}, {goal_y:.1f})')
        
        # Aguarda o servidor estar disponível
        self._action_client.wait_for_server()
        
        # Envia o goal de forma assíncrona
        self._send_goal_future = self._action_client.send_goal_async(goal_msg, feedback_callback=self.feedback_callback)
        
        # Configura callback para quando o goal for aceito/rejeitado
        self._send_goal_future.add_done_callback(self.goal_response_callback)
        
        self.is_executing = True
    
    def restart_sequence(self):
    
        """Reinicia a sequência de waypoints"""
        
        self.current_waypoint_index = 0
        self.is_executing = False
        self.send_next_waypoint()
    
    def goal_response_callback(self, future):
    
        """Callback quando o servidor responde ao goal"""
        
        goal_handle = future.result()
        
        if not goal_handle.accepted:
            self.get_logger().info(f'Waypoint {self.current_waypoint_index} rejeitado')
            self.is_executing = False
            
            # Tenta o próximo waypoint após 1 segundo
            self.schedule_next_waypoint(1.0)
            return
        
        self.get_logger().info(f'Waypoint {self.current_waypoint_index} aceito')
        
        # Configura callback para quando o resultado estiver pronto
        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)
    
    def retry_or_next(self):
    
        """Tenta novamente o mesmo waypoint ou passa para o próximo"""
        
        if self.current_waypoint_index < len(self.waypoints):
            self.send_next_waypoint()
    
    def get_result_callback(self, future):
    
        """Callback quando o resultado da ação está disponível"""
        
        result = future.result()
        
        if result.result.success:
            self.get_logger().info(f'Waypoint {self.current_waypoint_index} alcançado com sucesso!')
            
            # Incrementa para o próximo waypoint
            self.current_waypoint_index += 1
            
            # Aguarda 1 segundo antes de enviar o próximo waypoint
            self.is_executing = False
            self.schedule_next_waypoint(1.0)
        else:
            self.get_logger().warn(f'Falha ao alcançar waypoint {self.current_waypoint_index}')
            
            # Tenta o próximo waypoint após 2 segundos
            self.current_waypoint_index += 1
            self.is_executing = False
            self.schedule_next_waypoint(2.0)
    
    def feedback_callback(self, feedback_msg):
    
        """Callback para feedback da ação"""

        feedback = feedback_msg.feedback
        
        # Log periódico do feedback (a cada 10 feedbacks)
        if hasattr(self, 'feedback_counter'):
            self.feedback_counter += 1
            if self.feedback_counter % 10 == 0:
                self.get_logger().info(
                    f'Progresso waypoint {self.current_waypoint_index}: '
                    f'Posição atual ({feedback.current_x:.2f}, {feedback.current_y:.2f}), '
                    f'Distância: {feedback.distance_to_goal:.2f}'
                )
        else:
            self.feedback_counter = 0

    def schedule_next_waypoint(self, delay):
	
        """Agenda o próximo waypoint da lista com o temporizador"""
	
        if self.delay_timer is not None:
            return  # já existe um timer ativo

        self.delay_timer = self.create_timer(delay, self.send_next_waypoint_delayed)

    def send_next_waypoint_delayed(self, timer=None):
    
        """Callback do timer delay para publicar próximo waypoint"""
        
        if self.delay_timer is not None:
        	self.delay_timer.destroy()
        	self.delay_timer = None

        self.send_next_waypoint()
        
def main(args=None):

    rclpy.init(args=args)
    
    turtle_control_client = TurtleControlClient()
    
    try:
        rclpy.spin(turtle_control_client)
    except KeyboardInterrupt:
        turtle_control_client.get_logger().info('Cliente interrompido pelo usuário')
    finally:
        turtle_control_client.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
