from socket import *
from constCS import *
import threading
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


# Uma thread para cada requisição recebida
def handle_client(conn, addr):
    print(f"Cliente conectado: {addr}")

    while True:
        data = conn.recv(1024)
        if not data:
            break

        start_time = time.time()

        msg = data.decode()
        print(f"Recebido de {addr}: {msg}")

        response = process_request(msg)

        end_time = time.time()
        processing_time = end_time - start_time

        full_response = (
            f"{response} | tempo servidor: {processing_time:.6f}s"
        )

        conn.send(full_response.encode())

    conn.close()
    print(f"Conexão encerrada: {addr}")


server = socket(AF_INET, SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(10)

print("Servidor multithread aguardando conexões")

while True:
    conn, addr = server.accept()

    thread = threading.Thread(
        target=handle_client,
        args=(conn, addr)
    )
    thread.start()