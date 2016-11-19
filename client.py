import socket
import time

HOST = 'localhost'
PORT = 50008
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.settimeout(1)
    for i in range(10):
        print('Sending', i + 1, 'ping...')
        past = time.time()
        message = 'PING ' + str(i+1) + " " + str(past)
        s.sendall(message.encode())
        try:
            data = s.recv(1024)
            print('Delay', (time.time() - past) * 1000, 'ms')
            print('Received', data.decode())
        except socket.timeout:
            print('Packet Lost!')
        time.sleep(1)
