from socket import *
from constCS import *
import time

def process_request(msg):
    parts = msg.split(" ", 1)
    command = parts[0].upper()

    if len(parts) > 1:
        data = parts[1]
    else:
        data = ""

    if command == "UPPER":
        return data.upper()

    elif command == "LOWER":
        return data.lower()

    elif command == "REVERSE":
        return data[::-1]

    elif command == "COUNT":
        return str(len(data))

    else:
        return "Comando inválido"


server = socket(AF_INET, SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(10)

print("Servidor single-thread aguardando conexões")


while True:
    conn, addr = server.accept()
    print("Conectado por:", addr)

    data = conn.recv(1024)

    if not data:
        conn.close()
        continue

    start_time = time.time()

    msg = data.decode()
    print("Recebido:", msg)

    response = process_request(msg)

    end_time = time.time()
    processing_time = end_time - start_time

    full_response = (
        f"{response} | tempo servidor: {processing_time:.6f}s"
    )

    conn.send(full_response.encode())
    conn.close()from socket import *
from constCS import *
import time

def process_request(msg):
    parts = msg.split(" ", 1)
    command = parts[0].upper()

    if len(parts) > 1:
        data = parts[1]
    else:
        data = ""

    if command == "UPPER":
        return data.upper()

    elif command == "LOWER":
        return data.lower()

    elif command == "REVERSE":
        return data[::-1]

    elif command == "COUNT":
        return str(len(data))

    else:
        return "Comando inválido"

s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

print("Servidor aguardando conexão ")

(conn, addr) = s.accept()
print("Conectado por:", addr)

while True:
    data = conn.recv(1024)
    if not data:
        break

    start_time = time.time()

    msg = data.decode()
    print("Recebido:", msg)

    response = process_request(msg)

    end_time = time.time()
    processing_time = end_time - start_time

    full_response = f"{response} | tempo servidor: {processing_time:.6f}s"

    conn.send(full_response.encode())

conn.close()
