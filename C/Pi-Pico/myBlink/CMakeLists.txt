cmake_minimum_required(VERSION 3.12)

# Pull in SDK (must be before project)
include(pico_sdk_import.cmake)

project(pico_examples C CXX ASM)
set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)

# Initialize the SDK
pico_sdk_init()

add_executable(myBlink
  myBlink.c
)

pico_enable_stdio_usb(myBlink 1)
pico_enable_stdio_uart(myBlink 1)

pico_add_extra_outputs(myBlink)

target_link_libraries(myBlink pico_stdlib)

