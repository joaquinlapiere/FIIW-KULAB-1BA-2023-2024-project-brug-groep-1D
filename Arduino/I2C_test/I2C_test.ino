
#include <Wire.h>

void setup() {
  Wire.begin(0x0);
  Wire.onReceive(onReceive); // stel function in die geroepen wordt als er data binnenkomt via I2C
  Serial.begin(9600);
  Serial.println("serial started");
}

void loop(){}
// loop is leeg want er moet enkel data uitgelezen worden als er een signaal is
// loop moet blijven anders kan de compiler geen main functie maken


void onReceive() {
  char data = Wire.read();
  Serial.print(data);
}
