
const int vcc = 5;
float SensorValue;
float vout;
int gate = 0;

const unsigned long interval = 5000;
unsigned long lastUpdateTime = 0;
//DigitPot Pins
const int UD = 2;
const int INC = 3;
const int CS = 4;
float currentVoltage = 0;
float targetVoltage = 1.6;
float tol = 0.1;

//MUX Pins 
const int s0 = 9;
const int s1 = 8;
const int s2 = 7;
const int s3 = 6;
const int SIG = 5;
String content;
int val;
const int muxChannel[16][4] = { //{s3, s2, s1, s0}
	{0,0,0,0}, //C0
	{0,0,0,1}, //C1
	{0,0,1,0}, //C2
	{0,0,1,1}, //C3
	{0,1,0,0}, //C4
	{0,1,0,1}, //C5
	{0,1,1,0}, //C6
	{0,1,1,1}, //C7
	{1,0,0,0}, //C8
	{1,0,0,1}, //C9
	{1,0,1,0}, //C10
	{1,0,1,1}, //C11
	{1,1,0,0}, //C12
	{1,1,0,1}, //C13
	{1,1,1,0}, //C14
	{1,1,1,1} //C15
	};

float GetVoltage() {
  SensorValue = analogRead(A0);
  vout = (SensorValue / 1024) * 3.29;
	return vout;
}

void SetVoltage() {
  //Needs be loopable so only make 1 INC per loop
  currentVoltage = GetVoltage();

  digitalWrite(UD, 0);
  digitalWrite(CS, 0);
  if ((currentVoltage > targetVoltage + tol) || (currentVoltage < targetVoltage - tol)) {
    if (currentVoltage > targetVoltage) {
       digitalWrite(UD,0);
       //Serial.println("Going Down!");
    }
    else {
      digitalWrite(UD, 1);
      //Serial.println("Going Up!");
    }

    //Send pulse
    digitalWrite(INC,1);
    delay(1);
    digitalWrite(INC,0);
    delay(1);
  }
}
void ChangeDir() {
  if (targetVoltage == 0.4) {
    targetVoltage = 2.8;
  }
  else {
    targetVoltage = 0.4;
  }
}

void SetChannel(int channel) {
	digitalWrite(s0, muxChannel[channel][3]);
	digitalWrite(s1, muxChannel[channel][2]);
	digitalWrite(s2, muxChannel[channel][1]);
	digitalWrite(s3, muxChannel[channel][0]);
}

void SetTargetVoltage(float newVoltage) {
  targetVoltage = newVoltage;
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(A0, INPUT);
  
  pinMode(s0, OUTPUT);
  pinMode(s1, OUTPUT);
  pinMode(s2, OUTPUT);
  pinMode(s3, OUTPUT);
  pinMode(SIG, OUTPUT);

  pinMode(UD, OUTPUT);
  pinMode(CS, OUTPUT);
  pinMode(INC, OUTPUT);

  Serial.println("Starting: SerialToController.ino");
  SetChannel(15);
  SetTargetVoltage(1.5);
}

void loop() {
  //Voltage Correctio
  SetVoltage();

  while (Serial.available()){
    Serial.println("SerialIsAvaliable");
    content = Serial.readStringUntil('\n');
    if (content[0] == 'J') {
      if (content == "JU") {
        SetTargetVoltage(2.8);
      }
      if (content == "JN") {
        SetTargetVoltage(1.5);
      }
      if (content == "JD") {
        SetTargetVoltage(0.4);
      }
    }
    else {
      val = content.toInt();
      if ((val >= 0) && (val < 16)) {
        
        SetChannel(val);
        
        digitalWrite(SIG, 1);
        delay(250);
        digitalWrite(SIG, 0);
        delay(10);

        content = -1;
      }
    }
    
  }
}

