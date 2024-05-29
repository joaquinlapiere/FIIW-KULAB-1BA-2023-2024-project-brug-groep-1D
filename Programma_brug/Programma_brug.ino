#include <Wire.h>  // Importeert de Wire-bibliotheek voor I2C-communicatie

// Pinnen declareren
const int motorOphalen = 3; // Pin D3 voor motor omhoog
const int motorNeerhalen = 4; // Pin D4 voor motor omlaag
const int knopOmhoog = 7; // Pin D7 voor knop omhoog
const int knopOmlaag = 6; // Pin D6 voor knop omlaag
const int Buzzer = 12; // Pin D12 voor buzzer
const int Groen = 8; // Pin D8 voor groene LED
const int Blauw = 9; // Pin D9 voor blauwe LED
const int Rood = 10;  // Pin D10 voor rode LED

const int MPU6050_ADDR = 0x68; // I2C-adres van de MPU6050
const int ACCEL_XOUT_H = 0x3B; // Registeradres voor accelerometer X-uitgang

float acc_x, acc_y, acc_z;    // Variabelen voor accelerometerwaarden
float x_angle;  // Variabele voor berekende hoek
const float rad_to_deg = 180.0 / 3.14159265359;  // Omrekeningsfactor van radialen naar graden
const float marge = 3.0; // Marge voor hoeken instellen

void setup() {
  Serial.begin(9600);  // Start de seriële monitor met een baudrate van 9600
  Wire.begin(); // Start de I2C-communicatie
  
  Wire.beginTransmission(MPU6050_ADDR); // Start communicatie met MPU6050
  Wire.write(0x6B);  // Selecteer het PWR_MGMT_1 register
  Wire.write(0);  // Schakel de slaapmodus uit
  Wire.endTransmission(true); // Beëindig de transmissie
  
  // Stel de pinnen in als INPUT of OUTPUT
  pinMode(motorOphalen, OUTPUT);  // Stel motorOphalen in als output
  pinMode(motorNeerhalen, OUTPUT);  // Stel motorNeerhalen in als output
  pinMode(knopOmhoog, INPUT);   // Stel knopOmhoog in als input
  pinMode(knopOmlaag, INPUT);   // Stel knopOmlaag in als input
  pinMode(Buzzer, OUTPUT);  // Stel de Buzzer in als output
  pinMode(Groen, OUTPUT);  // Stel de groene LED in als output
  pinMode(Blauw, OUTPUT);  // Stel de blauwe LED in als output
  pinMode(Rood, OUTPUT);   // Stel de rode LED in als output
}

void setColor(int roodwaarde, int groenwaarde, int blauwwaarde) {  // Functie om verkeerslichtkleur in te stellen (3 kleuren kunnen elke kleur maken)
  analogWrite(Rood, roodwaarde);  // Stel de helderheid van de rode LED in
  analogWrite(Groen, groenwaarde);  // Stel de helderheid van de groene LED in
  analogWrite(Blauw, blauwwaarde);  // Stel de helderheid van de blauwe LED in
}

void loop() {
  bool omhoogStatus = digitalRead(knopOmhoog);  // Lees de status van knopOmhoog (true of false)
  bool omlaagStatus = digitalRead(knopOmlaag);  // Lees de status van knopOmlaag (true of false)

  readMPU6050();  // Lees de gegevens van de MPU6050-sensor
  calculateXAngle();  // Bereken de hoek op basis van de accelerometerwaarden

  if (omhoogStatus && !omlaagStatus) {  // Als knopOmhoog ingedrukt is en knopOmlaag niet ingedrukt is
    digitalWrite(Buzzer, HIGH);  // Zet de buzzer aan
    delay(1000);  // Wacht 1 seconde
    digitalWrite(Buzzer, LOW);  // Zet de buzzer uit
    setColor(255, 165, 0); // Stel de kleur van het verkeerslicht in op oranje
    delay(1000);  // Wacht 1 seconde
    setColor(255, 0, 0); // Stel de kleur van het verkeerslicht in op rood

    if (x_angle <= 0.0 + marge) {  // Als de hoek binnen de vooraf ingestelde hoek plus marge is
      while (x_angle <= 30.0 + marge) {  // Terwijl de hoek binnen 30 graden plus marge is
        delay(500);  // Wacht 0,5 seconde
        digitalWrite(motorOphalen, HIGH);  // Zet motor omhoog aan
        digitalWrite(motorNeerhalen, LOW);  // Zet motor omlaag uit

        readMPU6050();  // Lees de MPU6050-sensor 
        calculateXAngle();  // Bereken de hoek 

        Serial.print("Ophalen: ");  // Print "Ophalen: " naar de seriële monitor
        Serial.println(x_angle);  // Print de huidige hoek naar de seriële monitor

        delay(50);  // Wacht 0,05 seconden
      }
      digitalWrite(motorOphalen, LOW);  // Zet motor omhoog uit
    }
    setColor(255, 0, 0); // Stel de kleur van het verkeerslicht in op rood
    digitalWrite(Buzzer, HIGH);  // Zet de buzzer aan
    delay(1000);  // Wacht 1 seconde
    digitalWrite(Buzzer, LOW);  // Zet de buzzer uit
    
  } else if (omlaagStatus && !omhoogStatus) {  // Als knopOmlaag ingedrukt is en knopOmhoog niet is ingedrukt
    setColor(255, 0, 0); // Stel de kleur van het verkeerslicht in op rood
    digitalWrite(Buzzer, HIGH);  // Zet de buzzer aan
    delay(1000);  // Wacht 1 seconde
    digitalWrite(Buzzer, LOW);  // Zet de buzzer uit

    if (x_angle >= 30.0 - marge) {  // Als de hoek binnen 30 graden min een marge is
      while (x_angle >= 0.0 + marge) {  // Terwijl de hoek binnen 0 graden plus marge is
        digitalWrite(motorOphalen, LOW);  // Zet motor omhoog uit
        digitalWrite(motorNeerhalen, HIGH);  // Zet motor omlaag aan

        readMPU6050();  // Lees de MPU6050-sensor 
        calculateXAngle();  // Bereken de hoek 

        Serial.print("Neerhalen: ");  // Print "Neerhalen: " naar de seriële monitor
        Serial.println(x_angle);  // Print de huidige hoek naar de seriële monitor

        delay(50);  // Wacht 0,05 seconden
      }
      digitalWrite(motorNeerhalen, LOW);  // Zet motor omlaag uit
    }
    delay(1000);  // Wacht 1 seconde
    setColor(0, 255, 0); // Stel de kleur van het verkeerslicht in op groen
    digitalWrite(Buzzer, HIGH);  // Zet de buzzer aan
    delay(1000);  // Wacht 1 seconde
    digitalWrite(Buzzer, LOW);  // Zet de buzzer uit

  } else {
    digitalWrite(motorOphalen, LOW);  // Zet motor omhoog uit
    digitalWrite(motorNeerhalen, LOW);  // Zet motor omlaag uit
  }

  String omhoogStatusStr = omhoogStatus ? "aan" : "uit";  // Converteer omhoogStatus naar string 
  String omlaagStatusStr = omlaagStatus ? "aan" : "uit";  // Converteer omlaagStatus naar string
  Serial.print("x hoek = ");  // Print "x hoek = " naar de seriële monitor
  Serial.print(x_angle);  // Print de huidige hoek naar de seriële monitor
  Serial.print(", KnopOmhoog = ");  // Print ", KnopOmhoog = " naar de seriële monitor
  Serial.print(omhoogStatusStr);  // Print de status van knopOmhoog naar de seriële monitor
  Serial.print(", KnopOmlaag = ");  // Print ", KnopOmlaag = " naar de seriële monitor
  Serial.println(omlaagStatusStr);  // Print de status van knopOmlaag naar de seriële monitor en sluit printlijn af (println)

  delay(100);  // Wacht 100 milliseconden
}

void readMPU6050() {
  Wire.beginTransmission(MPU6050_ADDR);  // Start communicatie met MPU6050
  Wire.write(ACCEL_XOUT_H);  // Vraag de accelerometer X-uitgang aan
  Wire.endTransmission(false);  // Beëindig de transmissie, maar houd de I2C-bus actief
  Wire.requestFrom(MPU6050_ADDR, 6, true);  // Vraag 6 bytes aan van de MPU6050
  
  acc_x = (Wire.read() << 8 | Wire.read()) / 16384.0;  // Lees en combineer de hoge en lage bytes van acc_x
  acc_y = (Wire.read() << 8 | Wire.read()) / 16384.0;  // Lees en combineer de hoge en lage bytes van acc_y
  acc_z = (Wire.read() << 8 | Wire.read()) / 16384.0;  // Lees en combineer de hoge en lage bytes van acc_z
}

void calculateXAngle() {
  x_angle = atan2(acc_y, sqrt(acc_x * acc_x + acc_z * acc_z)) * rad_to_deg;  // Bereken de hoek op basis van acc_y, acc_x en acc_z
}