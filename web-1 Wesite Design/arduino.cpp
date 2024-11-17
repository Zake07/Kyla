const int capacitivePin = 2;    // Pin for capacitive sensor
const int irPin = 3;            // Pin for IR sensor

const int nonRecyclableLED = 5; // LED pin for non-recyclable waste

void setup() {
  pinMode(capacitivePin, INPUT);
  pinMode(irPin, INPUT);
  pinMode(nonRecyclableLED, OUTPUT);

  Serial.begin(9600);
}

void loop() {
  int capacitiveState = digitalRead(capacitivePin);
  int irState = digitalRead(irPin);

  if (capacitiveState == HIGH && irState == LOW) {
    Serial.println("Non-Recyclable Waste Detected");
    digitalWrite(nonRecyclableLED, HIGH);
  } 
  else {
    Serial.println("No Waste Detected");
    digitalWrite(nonRecyclableLED, LOW);
  }

  delay(1000);
}
#include <Servo.h>

int nonBioPin = 2;               // Non-Biodegradable Sensor Pin
int bioPin = 3;                  // Biodegradable Sensor Pin
int nonBioState = 0;             // Non-Biodegradable Sensor State
int bioState = 0;                // Biodegradable Sensor State
const int capacitivePin = 2;    // Pin for capacitive sensor
const int irPin = 3;            // Pin for IR sensor

const int nonRecyclableLED = 5; // LED pin for non-recyclable waste

Servo servoMotor;
int originalPosition = 90;       // Original position of the servo motor

void setup() {  
// Configure Sensor Pins
  pinMode(nonBioPin, INPUT);
  pinMode(bioPin, INPUT);
  pinMode(capacitivePin, INPUT);
  pinMode(irPin, INPUT);
  pinMode(nonRecyclableLED, OUTPUT);

  // Attach Servo Motor to Pin 9
  servoMotor.attach(9);

  // Set the servo motor to the original position
  servoMotor.write(originalPosition);
  
// Initialize Serial Communication
  Serial.begin(9600);
}

void loop() {
  // Read Sensor States
  nonBioState = digitalRead(nonBioPin);
  bioState = digitalRead(bioPin);
  int capacitiveState = digitalRead(capacitivePin);
  int irState = digitalRead(irPin);

  if (capacitiveState == HIGH && irState == LOW) {
    Serial.println("Non-Recyclable Waste Detected");
    digitalWrite(nonRecyclableLED, HIGH);

  else if  (nonBioState == HIGH && bioState == LOW) {
    Serial.println("Non-Biodegradable Material Detected");
    // Turn servo motor 90 degrees to the right
    servoMotor.write(0);
    delay(1000);
  }

  else if (bioState == HIGH && nonBioState == LOW) {
    Serial.println("Biodegradable Material Detected");
    // Turn servo motor 90 degrees to the left
    servoMotor.write(180);
    delay(1000);
  }
  
  else {
    // No material detected, return servo motor to original position
    servoMotor.write(originalPosition);
    delay(1000);
  }
}