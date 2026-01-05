from scapy.all import *
import os
from datetime import datetime
#Threadpool:
from concurrent.futures import *
import socket
import subprocess as sp

# ==== SETUP ====
#Networking Variables
NETWORK = os.getenv("network")
INTERFACE = os.getenv("ETHER_IFACE")
#INTERFACE = os.getenv("WIFI_IFACE")

#Set the desired NIC interface
conf.iface = INTERFACE

#common ports
PORTS = [80, 443, 21, 22, 53, 25, 110, 143, 993, 3389, 445, 135, 3306, 1433, 123, 139]

#==== FUNCTIONS ====
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

def open_ports(ip):
    open_ports = []

    for port in PORTS:
        try:
            with socket.create_connection((ip, port), timeout=0.1):
                open_ports.append(port)
        except:
            pass
    
    return open_ports
# === Get Device Name ===
def rDNS(ip):
    #The DNS must be setup on network, 
    # often not useable on home/non-configured networks
    try:
        return socket.gethostbyaddr(ip)[0]
    except:
        return None

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


def handle_functions(ip):
    data = [ip]
    ports = open_ports(ip)
    #name = rDNS(ip)
    name = nbtstat(ip)
    data.append(name)
    data.append(ports)
    return data
# ==== MAIN ====

#Create the exectuor:

ips = get_devices()

start_time = datetime.now()

#max_workers is max # of threads, for lan sockets:(50-64)
with ThreadPoolExecutor(max_workers=64) as executer:
    #futures contains the results of everything
    futures = []

    #For each ip, submit a request to use afunction
    for ip in ips:
        futures.append(executer.submit(handle_functions, ip))

    for future in as_completed(futures):
        print(future.result())

end_time = datetime.now()

time_elapsed = end_time - start_time

print(f"Done in {time_elapsed}.")


