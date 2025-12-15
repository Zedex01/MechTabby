from scapy.all import *
import os

PORTS = [80, 443, 21, 22, 53, 25, 110, 143, 993, 3389, 445, 135, 3306, 1433, 123, 139]

def netbios(ip):
    pkt = IP(dst=ip)/UDP(dport=137)/NBNSQueryRequest(QUESTION_NAME="*")
    ans = sr1(pkt, timeout=2, verbose=False)

    if ans and ans.haslayer(NBNSQueryResponse):
        return ans[NBNSQueryResponse].RR_NAME

    return None

def rev_dns(ip):
    #Dependant on setup
    try:
        return socket.gethostbyaddr(ip)[0]
    except:
        return None

def mDNS(ip):
    #Reliable for modern pcs (UDP).
    port = 5353
    pkt = (
        IP(dst=ip)/
        UDP(sport=RandShort(), dport=5353)/
        DNS(
            id=0,
            qr=0,
            opcode=0,
            rd=0,
            qd=DNSQR(qname="_services._dns-sd._udp.local", qtype="PTR")
            )
    )

    resp = sr(pkt, timeout=3, multi=True, verbose=False)[0]

    for _,r in resp:
        if r.haslayer(DNS):
            dns = r[DNS]
            if dns.an:
                for i in range(dns.ancount):
                    #return dns.an[i].rrname.decode(errors="ignore")
                    print(dns.an[i].rrname.decode(errors="ignore"))
                    exit()

def SMB(ip):
    #Good for windows
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect(ip, 445)

        #Minimal SMBv1 negotiate request
        smb_req = bytes.fromhex(
            "00000085ff534d427200000000180128000000000000000000000000000000000000000000000000"
            "000000000000000000000000024e54204c4d20302e313200"
        )       

        s.send(smb_req)
        data = s.recv(4096)
        s.close()

        #Look for ascii hostname:
        text = data.decode(errors="ignore")
        for token in text.split("\x00"):
            if token.isprintable() and len(token) > 3 and token.isupper():
                print(token)
    except:
        pass

def NBNS(ip):
    #Legacy, outdated
    pass

# RDNS -> SMB (port:445) -> mDNS -> NBNS

def port_open(ip, port):
    try:
        with socket.create_connection((ip, port), timeout=0.5):
            return True
    except:
        return False

#For this to work propely we reqiure NpCap to be installed (Windows)
NETWORK = os.getenv("network")

#Select WIFI or ETHERNET
INTERFACE = os.getenv("ETHER_IFACE")
#INTERFACE = os.getenv("WIFI_IFACE")

print("Network: ", repr(NETWORK))
print("Interface: ", repr(INTERFACE))

#Set Net Interface
conf.iface = INTERFACE

#create arp packet
arp = ARP(pdst=NETWORK)
ether = Ether(dst="ff:ff:ff:ff:ff:ff") #Broadcast

packet = ether/arp

#srp == Send at layer 2
result = srp(packet, timeout=2, verbose=False)[0]

clients = []

for sent, recv in result:
    clients.append({"ip":recv.psrc, "mac":recv.hwsrc})

print("Avalible Devices:")
for client in clients:
    print(f"IP:{client["ip"]}\tMAC:{client["mac"]}")
    print("Open Ports: ")
    for port in PORTS:
        if port_open(client["ip"], port):
            print(port, end="")
    print()



"""

getting names:;

Resolve-Dnsname -Name <ip>

(Get-CimInstance -ClassName Win32_ComputerSystem -ComputerName <ip>).Name
Write-Output 
"""