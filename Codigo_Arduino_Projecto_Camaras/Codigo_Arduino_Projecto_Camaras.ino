#include <Servo.h>

Servo myServo;
int receivedData = 0;  // Variable para almacenar el dato recibido
bool newData = false;  // Variable para verificar si hay un nuevo dato

void setup() {
  Serial.begin(9600);  // Inicializa la comunicación serial
  myServo.attach(9);   // Conecta el servomotor al pin 9
}

void loop() {
  // Verificar si hay datos en el puerto serial
  if (Serial.available() > 0) {
    receivedData = Serial.parseInt();  // Leer el dato enviado
    newData = true;                    // Indicar que hay un nuevo dato
  }

  // Si hay un nuevo dato, mover el servo
  if (newData) {
    if (receivedData > 0 && receivedData <= 180) {  // Validar rango de 0 a 180
      myServo.write(receivedData);  // Mover el servomotor al ángulo recibido
      Serial.print("Servo movido a: ");
      Serial.println(receivedData);  // Imprimir el ángulo movido en el monitor serial
    }
    newData = false;  // Resetear la bandera para esperar un nuevo dato
  }
  delay(10);
}