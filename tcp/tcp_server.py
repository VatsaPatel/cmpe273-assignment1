import socket, threading
from _thread import *

TCP_IP = '127.0.0.1'
TCP_PORT = 5000
BUFFER_SIZE = 1024

lock = threading.Lock()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((TCP_IP, TCP_PORT))

s.listen(1)
print("Server started at port:", TCP_PORT)

def getData(c, ClientID):
    while True:
        try:
            data = c.recv(1024)
            print(f"received data:{ClientID}:{data.decode()}")
            # send back reversed string to client
            c.send("pong".encode())
        except:
            print('Disconnected Client:', ClientID)
            break

    c.close()

while True:
    c, addr = s.accept()     # establish connection with client
    ClientID = c.recv(1024).decode()
    print('Connected Client:', ClientID)
    c.send("Start Sending".encode())
    start_new_thread(getData, (c,ClientID,))

s.close()