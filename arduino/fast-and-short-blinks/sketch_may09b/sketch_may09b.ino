void setup() {
  // put your setup code here, to run once:
  pinMode(13, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  // number of times to blink for each grouping
  int numOfBlinks = 5;
  // in milliseconds
  int fast = 500;
  int slow = 2000;

  // fast grouping
  for (int i = 0; i < numOfBlinks; i = i + 1) {
    digitalWrite(13, HIGH);
    delay(fast);
    digitalWrite(13, LOW);
    delay(fast);
  }
  
  // slow grouping
  for (int j = 0; j < numOfBlinks; j = j + 1) {
    digitalWrite(13, HIGH);
    delay(slow);
    digitalWrite(13, LOW);
    delay(slow);
  }
  
}
