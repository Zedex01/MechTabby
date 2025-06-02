cmake_minimum_required(VERSION 3.13)

# Refrence the SDK import
include($ENV{PICO_SDK_PATH}/external/pico_sdk_import.cmake)

#Create Project
project(helloUSB)

# Init the SDK
pico_sdk_init()

add_executable(helloUSB src/helloUSB.c)

target_include_directories(helloUSB PRIVATE
    ${CMAKE_CURRENT_LIST_DIR}/include
)


# Link stdlib and USB support
target_link_libraries(helloUSB
    pico_stdlib
    tinyusb_device
    tinyusb_board
)

pico_enable_stdio_usb(helloUSB 0) #Need to disbale to use HID
pico_enable_stdio_uart(helloUSB 0)

pico_add_extra_outputs(helloUSB)
