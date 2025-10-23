#include "Adafruit_TinyUSB.h"

Adafruit_USBD_HID usb_hid;

void setup() {
  usb_hid.begin();
  while (!USBDevice.mounted()) delay(10);
}

void loop() {
  uint8_t keycode[6] = {4, 0, 0, 0, 0, 0}; // 'A' key
  usb_hid.sendReport(0, keycode, sizeof(keycode)); // press A
  delay(100);
  memset(keycode, 0, sizeof(keycode));
  usb_hid.sendReport(0, keycode, sizeof(keycode)); // release
  delay(1000);
}
