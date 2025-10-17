import serial, time

class ConCom:

    def __init__(self, port):
        self.PORT = port
        self.BAUDRATE = 115200
        self.input_pause = 1
        self.ser = None
        self.button_map = {
                "d-up": "11",
                "d-right": "12",
                "d-down": "14",
                "d-left": "13",
                "x": "10",
                "a": "9",
                "b": "8",
                "y": "7",
                "lb": "6",
                "lt": "5",
                "rt": "4",
                "rb": "3",
                "+": "2",
                "-": "1",
                "home": "0",
                "ju": "JU",
                "jn": "JN",
                "jd": "JD",    
        }

        try:
            self.ser = serial.Serial(PORT, BAUDRATE)
            time.sleep(2)

        except Exception as e:
            print(f"Unable to mount: {e}")

    #Getters & Setters
    def get_port(self) -> int:
        return self.PORT

    def get_baudrate(self) -> int:
        return self.BAUDRATE

    def get_delay(self) -> int:
        return self.input_pause

    def set_port(self, port) -> None:
        self.PORT = port

    def set_baudrate(self, baudrate) -> None:
        self.BAUDRATE = baudrate

    def set_delay(self, delay) -> None:
        self.input_pause = delay

    #Functions
    def connect(self) -> None:
        try:
            self.ser = serial.Serial(PORT, BAUDRATE)
            time.sleep(2)

        except Exception as e:
            print(f"No Serial Found: {e}")

    def send(self, code) -> None:
        if check_connection():
            if code.upper() in [v.upper() for v in self.button_map.values()]:
                self.ser.write((code + '\n').encode())
            else:
                print("ERR: Not a valid key!")
        else:
            print("ERR: No Port Mounted!")
        
        time.sleep(self.input_pause)
    
    def check_connection(self) -> bool:
        return hasattr(self, "ser") and self.ser and self.ser.is_open

    