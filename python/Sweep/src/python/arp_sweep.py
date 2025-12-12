from scapy.all import ARP, Ether, srp, get_if_list, conf
import os

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