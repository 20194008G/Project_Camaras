import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
import time
class NodoPublicador(Node):
    def __init__(self):
        super().__init__("nodo_pub")
        self.publisher_ = self.create_publisher(Bool, "topico_1", 10)
        self.get_logger().info("Nodo publicador iniciado")
        msg = Bool()
        msg.data=True ##Codigo abrir puerta       
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publicando: "{msg.data}" para abrir la puerta')
        time.sleep(5)
        msg.data=False    
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publicando: "{msg.data}" para abrir la puerta')
def main(args=None):
    rclpy.init(args=args)
    nodo_publicador = NodoPublicador()
    rclpy.spin(nodo_publicador)
    nodo_publicador.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()