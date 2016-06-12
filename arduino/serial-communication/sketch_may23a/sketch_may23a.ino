void setup() {
  // put your setup code here, to run once:
  // set serial data transfer rate to 9600 bau
  Serial.begin(9600);
  // set pin 13 containing LED to output
  pinMode(13, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  // check if there is data in the serial buffer
  if (Serial.available() > 0) {
    char input = Serial.read();

    // if user enters the character 1 into serial monitor,
    // turn LED at pin 13 on
    if (input == '1') {
      digitalWrite(13, HIGH); 
    }

    // if user enters the character 0 into serial monitor,
    // turn LED at pin 13 off
    if (input == '0') {
      digitalWrite(13, LOW);
    }
  }
}
