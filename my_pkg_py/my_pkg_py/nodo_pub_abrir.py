import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool

class NodoPublicador(Node):
    def __init__(self):
        super().__init__("nodo_pub")
        self.publisher_ = self.create_publisher(Bool, "topico_1", 10)
        self.timer = self.create_timer(1, self.timer_callback)  # Publica cada 1 segundo
        self.get_logger().info("Nodo publicador iniciado")

    def timer_callback(self):
        msg = Bool()
        msg.data = True  # Código para abrir puerta
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publicando: "{msg.data}" para abrir la puerta')

def main(args=None):
    rclpy.init(args=args)
    nodo_publicador = NodoPublicador()
    rclpy.spin(nodo_publicador)  # Mantiene el nodo en funcionamiento hasta que lo detengas
    nodo_publicador.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
