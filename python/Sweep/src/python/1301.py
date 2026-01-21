#Matthew Moran  20205-01-13
#**REQUIRES PYTHON VERSION 3.11**
from scapy.all import *
import os
from datetime import datetime
#Threadpool:
from concurrent.futures import *
import socket
import subprocess as sp


from impacket.smbconnection import SMBConnection


# ==== SETUP ====
#Networking Variables
NETWORK = os.getenv("network")
INTERFACE = os.getenv("ETHER_IFACE")

#Set the desired NIC interface
conf.iface = INTERFACE

def get_devices():
    #Returns a list of all device ips

    devices = []

    #Broadcast ARP request to all devices on network:
    pkt = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=NETWORK)
    resp = srp(pkt, timeout=2, verbose=False)[0]
    
    for sent, recv in resp:
        pair = (recv.psrc, recv.hwsrc)

        devices.append(pair)

    return devices
    

def nbtstat(ip):
    #Command that returns device name
    cmd = ['nbtstat', '-A', ip]
    try:
        out = sp.check_output(cmd, stderr=sp.DEVNULL, text=True)

        for line in out.splitlines():
            # <00> UNIQUE = computer name
            if "<00>" in line and "UNIQUE" in line:
                return line.split()[0]

    except:
        return None
        
def rDNS(ip):
    #The DNS must be setup on network, 
    # often not useable on home/non-configured networks
    try:
        return socket.gethostbyaddr(ip)[0]
    except:
        return None

def smb_probe(ip):
    try:
        smb = SMBConnection(ip, ip, timeout=2)
        smb.login('', '')
        return smb.getServerName()
    except:
        return None

def handle_functions(ip):
    data = [ip]
    data.append(nbtstat(ip[0]))
    data.append(rDNS(ip[0]))
    data.append(smb_probe(ip[0]))
    
    
    return data






#Get IPs on network
ips = get_devices()

with ThreadPoolExecutor(max_workers=64) as executer:
    #futures contains the results of everything
    futures = []

    #For each ip, submit a request to use afunction
    for ip in ips:
        futures.append(executer.submit(handle_functions, ip))

    for future in as_completed(futures):
        print(future.result())