#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int16
import serial

class NodoSubscriptor(Node):
    def __init__(self):
        super().__init__("nodo_sub")
        # Inicializa el puerto serial
        self.serial_port = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)  # Ajusta el puerto a tu configuración
        self.subscription = self.create_subscription(Int16, "Rick", self.call, 10)
        self.get_logger().info("El nodo suscriptor ha sido iniciado")

    def call(self, var):
        # Envía el dato recibido al Arduino vía serial
        dato = var.data
        self.serial_port.write(f"{dato}\n".encode())  # Envía el dato al Arduino
        self.get_logger().info(f"Dato recibido: {dato}, enviado al Arduino")

def main(args=None):
    rclpy.init(args=args)
    node = NodoSubscriptor()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()