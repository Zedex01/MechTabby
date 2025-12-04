#define SENSOR 7
#define LED 9

int val;

void setup() {
  pinMode(LED, OUTPUT);
  pinMode(SENSOR, INPUT);
  
  Serial.begin(9600);
}

void loop() {
  val = digitalRead(SENSOR);

  if (val == HIGH){
    digitalWrite(LED, 1);
    
  }
  else {
    digitalWrite(LED, 0);
  }
  
  Serial.println(val);

}
