import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class NodoPublicador(Node):
    def __init__(self):
        super().__init__("nodo_pub")
        self.publisher_ = self.create_publisher(Int16, "topico_1", 10)
        self.timer = self.create_timer(1, self.timer_callback)
        self.contador = 1
        self.get_logger().info("Nodo publicador iniciado")
        self.minus = 1

    def timer_callback(self):
        msg = Int16()
        msg.data = self.contador
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publicando: "{msg.data}"')
        paso = 0
        
        if self.contador == 1:
            self.contador = 10
            paso = 1
        elif self.contador == 180 :
            self.minus = -1 
        elif self.contador == 10 and self.minus == -1:
            self.contador = 1
            self.minus = 1
            paso = 1
        if not paso:
            self.contador = self.contador + 10 * self.minus    
        
        
def main(args=None):
    rclpy.init(args=args)
    nodo_publicador = NodoPublicador()
    rclpy.spin(nodo_publicador)
    nodo_publicador.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()