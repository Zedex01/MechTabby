import ipaddress,platform,socket,subprocess as sp
from concurrent.futures import ThreadPoolExecutor
import os

#NETWORK = "192.168.1.0/24"
NETWORK = os.getenv("network")

PORTS = [80, 554]

TIMEOUT = 0.3

def ping(ip):
    cmd = ["ping", "-n", "1", "-w", "300", str(ip)]

    return sp.run(cmd, stdout=sp.DEVNULL, stderr=sp.DEVNULL).returncode == 0


#Try to open port and see if it is active
def port_open(ip, port):
    try:
        with socket.create_connection((str(ip), port), timeout=TIMEOUT):
            return True
    except:
        return False

def alive(ip):
    if ping(ip):
        return True
    for p in PORTS:
        if port_open(ip, p):
            return True
    return False


def main():
    net = ipaddress.ip_network(NETWORK, strict=False)
    print("Scanning Network...")
    taken = set()


    with ThreadPoolExecutor(max_workers=100) as ex:
        results = ex.map(alive, net.hosts())
        for ip, status in zip(net.hosts(), results):
            if status:
                taken.add(str(ip))
        

        free = [str(ip) for ip in net.hosts() if str(ip) not in taken]

        print("\nFree IPs:")
        for ip in free[:50]:
            print(ip)

        print(f"Total Free: {len(free)}")



if __name__ == "__main__":
    main()
