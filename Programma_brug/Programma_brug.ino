#include <Wire.h>

const int motorOphalen = 3;
const int motorNeerhalen = 4;
const int knopOmhoog = 7;
const int knopOmlaag = 6;
const int Buzzer = 12;
const int Groen = 8;
const int Blauw = 9;
const int Rood = 10;

const int MPU6050_ADDR = 0x68;
const int ACCEL_XOUT_H = 0x3B;

float acc_x, acc_y, acc_z;
float x_angle;
const float rad_to_deg = 180.0 / 3.14159265359;
const float marge = 3.0; 

void setup() {
  Serial.begin(9600);
  Wire.begin();
  
  Wire.beginTransmission(MPU6050_ADDR);
  Wire.write(0x6B); 
  Wire.write(0); 
  Wire.endTransmission(true);
  
  pinMode(motorOphalen, OUTPUT);
  pinMode(motorNeerhalen, OUTPUT);
  pinMode(knopOmhoog, INPUT);
  pinMode(knopOmlaag, INPUT);
  pinMode(Buzzer, OUTPUT);
  pinMode(Groen, OUTPUT);
  pinMode(Blauw, OUTPUT);
  pinMode(Rood, OUTPUT);

}
void setColor(int roodwaarde, int groenwaarde,  int blauwwaarde) {
  analogWrite(Rood, roodwaarde);
  analogWrite(Groen,  groenwaarde);
  analogWrite(Blauw, blauwwaarde);
}
void loop() {

  bool omhoogStatus = digitalRead(knopOmhoog);
  bool omlaagStatus = digitalRead(knopOmlaag);

  readMPU6050();
  calculateXAngle();


  if (omhoogStatus && !omlaagStatus) {              //ophalen
      digitalWrite(Buzzer, HIGH);
      delay(1000);
      digitalWrite(Buzzer,LOW);
      setColor(255, 165, 0); // Oranje 
      delay(1000);
      setColor(255, 0, 0); // Rood
    if (x_angle <= 3.0 + marge) {
      while (x_angle <= 45.0 + marge) {
        delay(500);
        digitalWrite(motorOphalen, HIGH);
        digitalWrite(motorNeerhalen, LOW);

        readMPU6050();
        calculateXAngle();

        Serial.print("Ophalen: ");
        Serial.println(x_angle);

        delay(50);
      }
      digitalWrite(motorOphalen, LOW);
      }
      setColor(255, 0, 0); // Rood
      digitalWrite(Buzzer,HIGH);
      delay(1000);
      digitalWrite(Buzzer, LOW);
    
  } else if (omlaagStatus && !omhoogStatus) {          //neerhalen
        setColor(255, 0, 0); // Rood
        digitalWrite(Buzzer, HIGH);
        delay(1000);
        digitalWrite(Buzzer, LOW);
    if (x_angle >= 45.0 - marge) {
      while (x_angle >= 3.0 + marge) {
        digitalWrite(motorOphalen, LOW);
        digitalWrite(motorNeerhalen, HIGH);

        readMPU6050();
        calculateXAngle();

        Serial.print("Neerhalen: ");
        Serial.println(x_angle);

        delay(50);
      }
      digitalWrite(motorNeerhalen, LOW);
      }
      delay(1000);
      setColor(0,  255, 0); // Groen
      digitalWrite(Buzzer, HIGH);
      delay(1000);
      digitalWrite(Buzzer, LOW);

  } else {
    digitalWrite(motorOphalen, LOW);
    digitalWrite(motorNeerhalen, LOW);
  }

  String omhoogStatusStr = omhoogStatus ? "aan" : "uit";
  String omlaagStatusStr = omlaagStatus ? "aan" : "uit";
  Serial.print("x hoek = ");
  Serial.print(x_angle);
  Serial.print(", KnopOmhoog = ");
  Serial.print(omhoogStatusStr);
  Serial.print(", KnopOmlaag = ");
  Serial.println(omlaagStatusStr);

  delay(100); 
}

void readMPU6050() {
  Wire.beginTransmission(MPU6050_ADDR);
  Wire.write(ACCEL_XOUT_H);
  Wire.endTransmission(false);
  Wire.requestFrom(MPU6050_ADDR, 6, true);
  
  acc_x = (Wire.read() << 8 | Wire.read()) / 16384.0;
  acc_y = (Wire.read() << 8 | Wire.read()) / 16384.0;
  acc_z = (Wire.read() << 8 | Wire.read()) / 16384.0;
}

void calculateXAngle() {
  x_angle = atan2(acc_y, sqrt(acc_x * acc_x + acc_z * acc_z)) * rad_to_deg;
}
