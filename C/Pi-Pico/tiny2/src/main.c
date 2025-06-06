#include "bsp/board.h"
#include "tusb.h"

/*	 For Sending Reports to host:
	tud_hid_keyboard_report(id, modifer, &keycode);
	id = report id, normally 0 for single keyboard
	modifer = 0: indicates no control, shift, etc...
	
	modifier for left shift:  KEYBOARD_MODIFIER_LEFTSHIFT
*/

//Function for sending key to the device
void send_key(uint8_t keycode) {
    tud_hid_keyboard_report(0, 0, &keycode); //Depress Key 
    sleep_ms(10);
    tud_hid_keyboard_report(0, 0, NULL); //Release Key
    sleep_ms(10);
}

int main() {
    board_init(); //Init board
    tusb_init(); //Init TinyUSB

    absolute_time_t start = get_absolute_time(); //For clock, getting timing
    bool sent = false; //flag to insure it is only sent once

    while (1) {
        tud_task();  // Let TinyUSB process USB events

        if (!sent && absolute_time_diff_us(start, get_absolute_time()) > 5 * 1000 * 1000) {
            send_key(HID_KEY_H);
            send_key(HID_KEY_E);
            send_key(HID_KEY_L);
            send_key(HID_KEY_L);
            send_key(HID_KEY_O);
            send_key(HID_KEY_COMMA);
            send_key(HID_KEY_SPACE);
            send_key(HID_KEY_W);
            send_key(HID_KEY_O);
            send_key(HID_KEY_R);
            send_key(HID_KEY_L);
            send_key(HID_KEY_D);
            send_key(HID_KEY_1); // '!' requires shift if you want exact char
            sent = true;
        }
    }
}
