"""

TARGET IP FULL SCAN:




"""
from scapy.all import *
import socket

TARGET = input("Enter the target IP: ")

def get_mac(ip):
    pkt= Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip) #Broadcast

    ans = srp(pkt, timeout = 2, verbose = False)[0]

    if ans:
        return ans[0][1].hwsrc
    return None

#Scan for open ports
def syn_scan(ip, ports):
    open_ports = []
    for p in ports:
        pkt = IP(dst=ip)/TCP(dport=p, flags="S")
        recv = sr1(pkt, timeout=0.4, verbose=False)

        if recv and recv.haslayer(TCP):
            flags = recv

mac = get_mac(TARGET)
print(mac)