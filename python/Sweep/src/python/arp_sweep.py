from scapy.all import ARP, Ether, srp
import os

#For this to work propely we reqiure NpCap to be installed (Windows)

NETWORK = os.getenv("network")

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