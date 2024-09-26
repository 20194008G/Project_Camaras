import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
import serial
class NodoSuscritor(Node):
    def __init__(self):
        super().__init__("nodo_sub")
        self.serial_port = serial.Serial('/dev/ttyACM1', 9600, timeout=1)  # Ajusta el puerto a tu configuración
        self.subscription = self.create_subscription(
            Bool(),
            "topico_1",
            self.listener_callback,
            10)
        self.get_logger().info("Nodo suscriptor iniciado")

    def listener_callback(self, msg):
        msg.data
        dato = msg.data
        if dato==False: dato_servo=1
        if dato==True: dato_servo=120
        self.serial_port.write(f"{dato_servo}\n".encode())  # Envía el dato al Arduino
        self.get_logger().info(f"Dato recibido: {dato}, enviado al Arduino")

def main(args=None):
    rclpy.init(args=args)
    nodo_suscritor = NodoSuscritor()
    rclpy.spin(nodo_suscritor)
    nodo_suscritor.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()