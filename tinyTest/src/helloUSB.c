/*
* 
* 2025 5 30
* 
*/

#include "bsp/board.h"
#include "tusb.h"
#include <string.h>

const char* str = "Hello, World!\n";
uint8_t usb_index = 0;
bool sent = false;

void send_char(char c){
	uint8_t keycode = 0;
	
	if (c >= 'a' && c <= 'z') keycode = HID_KEY_A + (c - 'a');
	else if (c >= 'A' && c <= 'Z') keycode = HID_KEY_A + (c - 'A');
	else if (c == ' ') keycode = HID_KEY_SPACE;
	else if (c == ',') keycode = HID_KEY_COMMA;
	else if (c == '.') keycode = HID_KEY_PERIOD;
	else if (c == '\n') keycode = HID_KEY_ENTER;
	
	bool shift = (c >= 'A' && c <= 'Z');
	
	tud_hid_keyboard_report(0, shift ? KEYBOARD_MODIFIER_LEFTSHIFT : 0, &keycode);
}


//Checks the content of str, if there are still chars to send, send them!
void hid_task(void){
	if (!tud_hid_ready() || sent) return;
	
	if (usb_index < strlen(str)) {
		char c = str[usb_index++];
		send_char(c);
	} else if (usb_index == strlen(str)) {
		tud_hid_keyboard_report(0, 0, NULL);
		sent = true;
	}
}

int main() {
	board_init(); //Initialize pi-pico
	tusb_init(); //Initiakize tinyusb
	
	while(1) {
		tud_task(); //Handle USB tasks
		hid_task();
		
	}
}




/*
Device Descriptor:
	Identifies the USB device type (vendor ID, product ID, 
	version, number of configurations, etc.).

Configuration Descriptor:
	Describes a USB configuration: 
	how many interfaces it has, power requirements, etc.

Interface Descriptor(s):
	Describe a function like HID, CDC, MSC, etc. 
	Each interface is like a "virtual device."

Endpoint Descriptor(s):
	Define the pipes used to transfer data (IN/OUT endpoints, size, type).

HID Decsriptor:
	(For HID devices only) Describes HID class info and 
	references the HID report descriptor.
	
Report Discriptor:
	Describes the format of the data sent/received over HID 
	(e.g., keyboard scan codes).

String Descriptor:
	Optional but common — provide human-readable strings (like "Manufacturer").

Required to Implement (TinyUSB):	
	
| Function                                  | Required For        | Purpose                                                                                                  |
| ----------------------------------------- | ------------------- | -------------------------------------------------------------------------------------------------------- |
| `tud_descriptor_device_cb()`              | All devices         | Returns a pointer to the **device descriptor**.                                                          |
| `tud_descriptor_configuration_cb(index)`  | All devices         | Returns pointer to the **configuration descriptor** (and everything it includes: interfaces, endpoints). |
| `tud_descriptor_string_cb(index, langid)` | Optional but common | Returns a UTF-16LE encoded **string descriptor**.                                                        |
| `tud_hid_descriptor_report_cb(instance)`  | HID devices only    | Returns pointer to the **HID report descriptor** (layout of HID reports).                                |


*/
// Keyboard HID report descriptor
const uint8_t hid_report_descriptor[] = {
    TUD_HID_REPORT_DESC_KEYBOARD()
};


// Provide descriptor to TinyUSB
uint8_t const* tud_hid_descriptor_report_cb(uint8_t instance) {
    (void)instance; // Avoid unused warning (TinyUSB only uses 1 instance)
    return hid_report_descriptor;
}
//Required HID descriptor callbacks

// Called when the host requests a HID report
uint16_t tud_hid_get_report_cb(uint8_t instance,
                               uint8_t report_id,
                               hid_report_type_t report_type,
                               uint8_t* buffer,
                               uint16_t reqlen) {
    // Fill in report if needed
    return 0; // Return actual report length
}

