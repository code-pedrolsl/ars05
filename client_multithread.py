from socket import *
from constCS import *
import threading
import random
import string
import time

TOTAL_REQUISICOES = 100


# gera string aleatória

def random_text(size=10):
    return ''.join(random.choices(string.ascii_letters, k=size))


# gera comando aleatório

def generate_request():
    commands = ["UPPER", "LOWER", "REVERSE", "COUNT"]
    command = random.choice(commands)
    text = random_text()
    return f"{command} {text}"


# cada requisição vai em uma nova thread

def send_request(req_id):
    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((HOST, PORT))

        request = generate_request()

        start_time = time.time()

        s.send(request.encode())
        response = s.recv(1024).decode()

        end_time = time.time()
        total_time = end_time - start_time

        print(
            f"Req {req_id}: {request} -> {response} "
            f"| tempo cliente: {total_time:.6f}s"
        )

        s.close()

    except Exception as e:
        print(f"Erro na requisição {req_id}: {e}")


threads = []

experiment_start = time.time()

for i in range(TOTAL_REQUISICOES):
    t = threading.Thread(target=send_request, args=(i + 1,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

experiment_end = time.time()

print(
    f"\nTempo total do experimento: "
    f"{experiment_end - experiment_start:.6f}s"
)