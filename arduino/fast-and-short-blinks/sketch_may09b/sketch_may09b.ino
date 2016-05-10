void setup() {
  // put your setup code here, to run once:
  pinMode(13, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  // call blink
  blink(13, 5, 500);
  blink(13, 5, 2000);
  
}

void blink(int pinNumber, int numOfBlinks, int speedInMilliseconds) {
  for (int i = 0; i < numOfBlinks; i++) {
    digitalWrite(pinNumber, HIGH);
    delay(speedInMilliseconds);
    digitalWrite(pinNumber, LOW);
    delay(speedInMilliseconds);
  }
}
