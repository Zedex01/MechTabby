#include "tusb.h"

// Called when the host sends a SET_REPORT request (e.g., to send LED state to keyboard)
void tud_hid_set_report_cb(uint8_t instance, uint8_t report_id,
                           hid_report_type_t report_type,
                           uint8_t const* buffer, uint16_t bufsize) {
    // Optional: handle the incoming report from the host here
    (void)instance;
    (void)report_id;
    (void)report_type;
    (void)buffer;
    (void)bufsize;
    // Example: print or store the received data
}

// Called when the host requests a GET_REPORT (e.g., to poll input report)
uint16_t tud_hid_get_report_cb(uint8_t instance, uint8_t report_id,
                               hid_report_type_t report_type,
                               uint8_t* buffer, uint16_t reqlen) {
    // Optional: fill buffer with report data the host requested
    (void)instance;
    (void)report_id;
    (void)report_type;
    (void)reqlen;

    // Example: return 0 to indicate no data (or you could return dummy report)
    return 0;
}

