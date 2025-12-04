import serial, time
import serial.tools.list_ports
def main():

    #Find all devices:
    ports = serial.tools.list_ports.comports()

    arduino_port = ""

    for port in ports:
        if "Leonardo" in port.description:
            print("Found device on ", port.device)
            arduino_port = port.device
    try:
        ser = serial.Serial(arduino_port, 9600, timeout=1)
        print("Connected to port ", ser.portstr)
        #Give time for connection to establish
        time.sleep(2)

        while ser:
            ser.reset_input_buffer()
            response = ""
            
            while response == "":
                response = ser.readline().decode('utf-8').strip()
                time.sleep(0.1)
            
            print("Received: ", response)

            time.sleep(1)

        ser.close()
    
    except Exception as e:
        print(e)



if __name__ == "__main__":
    main()