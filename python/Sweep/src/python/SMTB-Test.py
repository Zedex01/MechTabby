import socket

def test_smtb(ip, port=25):
    s = socket.create_connection((ip,port), timeout=2)
    f = s.makefile("rwb", buffering=0)

    s.sendall(b"HELO test\r\n")
    
    try:
        resp = s.recv(1024).decode(errors="ignore")
        print("HELO resp: ", resp.strip())
    
    except socket.timeout:
        print("No Response...")

    s.close()


def test_port(ip, port):
    s = socket.create_connection((ip, port), timeout=3)

    try:
        print(s.recv(1024).decode(errors="ignore"))
    except:
        print("No banner") 

TARGET = input("Insert Target IP: ")
PORT = input("Port: ")
 
test_port(TARGET, PORT)
