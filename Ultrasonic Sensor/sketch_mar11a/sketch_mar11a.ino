int pinTrig = 2;
int pinEcho = 3;
long temps;
float distance;


void setup() {
  pinMode(pinTrig, OUTPUT);
  pinMode(pinEcho, INPUT);

  digitalWrite(pinTrig, LOW);

  Serial.begin(9600);
}


void loop() {
  digitalWrite(pinTrig, HIGH);
  delayMicroseconds(10);
  digitalWrite(pinTrig, LOW);

  temps = pulseIn(pinEcho, HIGH);

  if (temps > 25000) {
    Serial.println("Echec de la mesure");
  }

  else {
    temps = temps/2;
    distance = (temps*340)/10000.0;
    Serial.print("Distance: ");
    Serial.print(distance);
    Serial.println(" cm");
  }
  delay(2000);
}

