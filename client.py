from socket import *
from constCS import *
import time

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    msg = input("Digite comando (ou exit): ")
    if msg == "exit":
        break

    start_time = time.time()

    s.send(msg.encode())
    data = s.recv(1024)

    end_time = time.time()
    total_time = end_time - start_time

    print("Resposta:", data.decode())
    print(f"Tempo total (cliente): {total_time:.6f}s\n")

s.close()
