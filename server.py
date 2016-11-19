import socket
import random
import time

HOST = ''  # host
PORT = 50008  # port
LOSS_RATE = 0.3
AVERAGE_DELAY = .100  # time in seconds


def loss():
    if random.random() < LOSS_RATE:
        return True
    else:
        return False

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    print('Server initiated')
    while True:
        s.listen(1)
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                time.sleep(random.random() * 2 * AVERAGE_DELAY)
                if not data: break
                if not loss(): conn.sendall(data)
