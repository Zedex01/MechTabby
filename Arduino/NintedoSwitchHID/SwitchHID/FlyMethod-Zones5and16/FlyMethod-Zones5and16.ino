
#include "switch_tinyusb.h"
Adafruit_USBD_HID G_usb_hid;
NSGamepad Gamepad(&G_usb_hid); // Create Instance Of Gamepad

#define NSButton_NONE 0xFF

#define SEQ_NONE 0xFF
#define SEQ_DP_UP 100
#define SEQ_DP_DOWN 101
#define SEQ_DP_LEFT 102
#define SEQ_DP_RIGHT 103

//Define Sequence:
const uint8_t startupSequence[] = {
  NSButton_A,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  NSButton_A,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  NSButton_A,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  NSButton_B,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_DP_UP,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_DP_LEFT,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_DP_LEFT,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  NSButton_A,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  NSButton_A,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  NSButton_A,  
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  NSButton_Plus,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  NSButton_Y,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  NSButton_Minus,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_DP_DOWN,
  SEQ_DP_DOWN,
  SEQ_DP_DOWN,
  SEQ_DP_DOWN,
  NSButton_A,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_DP_DOWN,
  SEQ_DP_DOWN,
  SEQ_DP_DOWN,
  SEQ_DP_DOWN,
  NSButton_A,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  NSButton_A,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE
};

const uint8_t loopSequence[] = {
  NSButton_Plus,
  SEQ_NONE,
  SEQ_NONE,
  NSButton_Y,
  SEQ_DP_DOWN,
  SEQ_DP_DOWN,
  SEQ_DP_DOWN,
  SEQ_DP_DOWN,
  NSButton_A,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  NSButton_A,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE,
  SEQ_NONE
};

//Get Sequence length
const int loopSequenceLength = sizeof(loopSequence) / sizeof(loopSequence[0]);
const int startupSequenceLength = sizeof(startupSequence) / sizeof(startupSequence[0]);

//Set delay between presses
const unsigned long delayTime = 250;
const unsigned long holdTime = 100;

int currentStep = 0;
unsigned long lastTime = 0;
bool startupDone = false;
bool buttonHeld = true;


void setup() {
  Gamepad.begin();

  // wait until device mounted
  while( !USBDevice.mounted() ) delay(1);
}


void loop() {
  unsigned long now = millis(); //Get current runtime

  //Decide which sequence we are on:
  const uint8_t* sequence = startupDone ? loopSequence : startupSequence;
  const int sequenceLength = startupDone ? loopSequenceLength : startupSequenceLength;

  //Check if it is time to press button!
  if (!buttonHeld && (now - lastTime >= delayTime)){
    //Press next button
    Gamepad.releaseAll();
    uint8_t btn = sequence[currentStep];
    if(btn == SEQ_NONE) {
      //do nothing
    }
    else if (btn >= 100){ //D-Pad
      switch(btn) {
        case SEQ_DP_UP: Gamepad.dPad(NSGAMEPAD_DPAD_UP); break;
        case SEQ_DP_RIGHT: Gamepad.dPad(NSGAMEPAD_DPAD_RIGHT); break;
        case SEQ_DP_LEFT: Gamepad.dPad(NSGAMEPAD_DPAD_LEFT); break;
        case SEQ_DP_DOWN: Gamepad.dPad(NSGAMEPAD_DPAD_DOWN); break;
      }
    }
    else {
      Gamepad.press(btn); //Normal Btn
    }

      //Send Report to switch:
    if (Gamepad.ready()) Gamepad.loop();
    
    buttonHeld = true;
    lastTime = now;
  }

  //release after holdtime:
  if (buttonHeld && (now - lastTime >= holdTime)){
    Gamepad.releaseAll();
    Gamepad.dPad(NSGAMEPAD_DPAD_CENTERED);
    if(Gamepad.ready()) Gamepad.loop();

    buttonHeld = false;
    //advance to next step:
    currentStep++;
    if (currentStep >= sequenceLength) {
      if (!startupDone) startupDone = true;
      currentStep = 0;
      }
  }
}
