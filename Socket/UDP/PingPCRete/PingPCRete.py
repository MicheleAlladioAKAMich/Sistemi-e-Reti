import threading, ipaddress, time, subprocess, os
from queue import Queue
from colorama import init

init()

printLock = threading.Lock()
netAddress = input("Inserisci un network address: ")
startTime = time.time()
ipNetwork = ipaddress.ip_network(netAddress)
all_hosts = list(ipNetwork.hosts())

try:
    info = subprocess.STARTUPINFO
    info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    info.wShowWindow = subprocess.SW_HIDE
except Exception:
    pass

print(f"Indirizzo di rete che vuoi pingare: {netAddress}")

def pingSweap(ip):
    if os.name == "nt":
        output = subprocess.Popen("ping", "-n", "1", "-w", "150", str(all_hosts[ip]), stdout=subprocess.PIPE, startupinfo=info).communicate()[0]

    with printLock:
        print('\033[93m', end='')

    if "Risposta" in output.decode("utf-8"):
        print(str(all_hosts[ip]), "\033[90m" + "is online")
    elif "Host di destinazione non raggiungibile" in output.decode('utf-8'):
        pass
    else :
        print("UNKNOWN", end='')

def threader():
    while True:
        worker = q.get()
        pingSweap(worker)
        q.task_done()

q = Queue()

for x in range (100):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

for worker in range(len(all_hosts)):
    q.put(worker)

q.join()

runtime = float("%0.2f"% (time.time() - startTime))
print(f"Runtime {runtime} seconds")