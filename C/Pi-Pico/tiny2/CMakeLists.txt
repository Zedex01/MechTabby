cmake_minimum_required(VERSION 3.13)
# Pull in the Pico SDK
include($ENV{PICO_SDK_PATH}/external/pico_sdk_import.cmake)
# Set the project name and target board
project(pico_numpad)



# Initialize the SDK
pico_sdk_init()

# Create the executable
add_executable(pico_numpad
    src/main.c
    src/usb_descriptors.c
	src/usb_callbacks.c
)

# Include paths
target_include_directories(pico_numpad PRIVATE
    ${CMAKE_CURRENT_LIST_DIR}/include
)

# Link libraries
target_link_libraries(pico_numpad
    pico_stdlib
    tinyusb_device
    tinyusb_board
)

# Enable UART or USB stdout
pico_enable_stdio_usb(pico_numpad 0)
pico_enable_stdio_uart(pico_numpad 1)

# Create UF2 file
pico_add_extra_outputs(pico_numpad)
