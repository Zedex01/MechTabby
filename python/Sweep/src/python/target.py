"""

TARGET IP FULL SCAN:

writing and clearing line:
sys.stdout.write('\x1b[1A') #Move cursor up 1
sys.stdout.write('\x1b[2k') #Clear line
sys.stdout.write('content')
sys.stdout.flush() #put on screen??


May not get results using only scapy since these are raw. windows blocks unsolicited packets.
so, use socket connect instead:

"""
from scapy.all import *
import socket, sys
from datetime import datetime

TARGET = input("Enter the target IP: ")

PORTS = [80, 443, 21, 22, 53, 25, 110, 143, 993, 3389, 445, 135, 3306, 1433, 123, 139]

NETWORK = os.getenv("network")
INTERFACE = os.getenv("ETHER_IFACE")
#INTERFACE = os.getenv("WIFI_IFACE")
print("Network: ", repr(NETWORK))
print("Interface: ", repr(INTERFACE))

conf.iface = INTERFACE

def get_mac(ip):
    pkt= Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip) #Broadcast

    ans = srp(pkt, timeout = 2, verbose = False)[0]

    if ans:
        return ans[0][1].hwsrc
    return None

def tcp_connect(ip, port):
    #Try socket connection
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(0.5)
    print("\tTrying TCP Connection...", end="")
    try:
        s.connect((ip,port))
        s.close()
        return True
    except Exception as e:
        print(f"\t{e}\t")
        return False

def ping(ip):
    reply = sr1(IP(dst=ip)/ICMP(), timeout=2, verbose=False)
    if reply:
        return True
    return False

def netbios(ip):
    pkt = IP(dst=ip)/UDP(dport=137)/NBNSQueryRequest(QUESTION_NAME="*")
    ans = sr1(pkt, timeout=2, verbose=False)

    if ans and ans.haslayer(NBNSQueryResponse):
        return ans[NBNSQueryResponse].RR_NAME

    return None
#Scan for open ports
def syn_scan(ip, ports):
    start_time = datetime.now()
    port_count = len(ports)

    open_ports = []
    for p in ports:
        pkt = IP(dst=ip)/TCP(dport=p, flags="S")
        ans = sr1(pkt, timeout=0.5, verbose=False)

        #sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')
        sys.stdout.write('\r') #Return to start of line
        sys.stdout.write(str(p))
        sys.stdout.flush()
        if ans and ans.haslayer(TCP):
            flags = ans.getlayer(TCP).flags
            if flags == 0x12: #SYN/ACK
                open_ports.append(p)
                #Send rst to be polite?
                send(IP(dst=ip)/TCP(dport=p, flags="R"), verbose=False)

        #else:
        #    #If no good, try a direct socket connection, gets passed firewalls
        #    if tcp_connect(ip, p):
        #        open_ports.append(p)

    
    sys.stdout.write('\n')

    return open_ports

mac = get_mac(TARGET)
print("MAC: ", mac)

#Check that device is pingable
if not ping(TARGET):
    print("Host Unreachable...")
    exit()
    
print("go_next!")

