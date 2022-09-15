#include <Wire.h>
#include <Adafruit_MLX90614.h>
Adafruit_MLX90614 mlx = Adafruit_MLX90614();
float data;
void setup() {
Serial.begin(9600);
//Serial.println("Adafruit MLX90614 test");
mlx.begin();
pinMode(6,OUTPUT);
pinMode(7,OUTPUT);
}
void loop() {
  digitalWrite(6,LOW);
  digitalWrite(7,LOW);
  data=mlx.readObjectTempC();
  Serial.print(data);
  if (data>37){
  Serial.println("*C CAUTION");
  digitalWrite(6,HIGH); digitalWrite(7,LOW);}
  else {
  Serial.println("*C SAFE"); digitalWrite(7,HIGH);
  digitalWrite(6,LOW);}
  Serial.println();
  delay(500);
}
