from socket import *
from constCS import *
import random
import string
import time

TOTAL_REQUISICOES = 100


def random_text(size=10):
    return ''.join(random.choices(string.ascii_letters, k=size))


def generate_request():
    commands = ["UPPER", "LOWER", "REVERSE", "COUNT"]
    command = random.choice(commands)
    text = random_text()
    return f"{command} {text}"


experiment_start = time.time()

for i in range(TOTAL_REQUISICOES):
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((HOST, PORT))

    request = generate_request()

    start_time = time.time()

    s.send(request.encode())
    response = s.recv(1024).decode()

    end_time = time.time()
    total_time = end_time - start_time

    print(
        f"Req {i + 1}: {request} -> {response} "
        f"| tempo cliente: {total_time:.6f}s"
    )

    s.close()

experiment_end = time.time()

print(f"Tempo total do experimento: "f"{experiment_end - experiment_start:.6f}s")