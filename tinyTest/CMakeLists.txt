cmake_minimum_required(VERSION 3.13)

# Refrence the SDK import
include($ENV{PICO_SDK_PATH}/external/pico_sdk_import.cmake)

# Init the SDK
pico_sdk_init()

project(my_usb_project)

add_executable(my_usb_project main.c)

# Link stdlib and USB support
target_link_libraries(my_usb_project
    pico_stdlib
    tinyusb_device
    tinyusb_board
)

pico_enable_stdio_usb(my_usb_project 1)
pico_enable_stdio_uart(my_usb_project 0)

pico_add_extra_outputs(my_usb_project)
