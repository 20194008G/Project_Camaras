#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
from example_interfaces.msg import Int16

class Nodo_publicador(Node):
    def __init__(self):
        super().__init__("nodo_publicador")
        self.contador=0
        self.p = self.create_publisher(Int16, "Rick", 10)
        self.timer_ = self.create_timer(3, self.publish_news)
        self.get_logger().info("News publisher has been started")

    def publish_news(self):
        self.contador+=1

        msg2 = Int16()
        msg2.data = self.contador
        self.p.publish(msg2)
        
def main(args=None):
    rclpy.init(args=args)
    node = Nodo_publicador()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()