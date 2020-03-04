import socket, time, sys

print(str(sys.argv))
TCP_IP = '127.0.0.1'
TCP_PORT = 5000
BUFFER_SIZE = 1024
MESSAGE = "ping"
DELAY = int(sys.argv[2])
MessageCount = int(sys.argv[3])
ClientId = sys.argv[1]

def send():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(f"{ClientId}".encode())
    if s.recv(BUFFER_SIZE).decode() == "Start Sending" :
        for x in range(MessageCount):
            print("Sending Data:", MESSAGE)
            s.send(MESSAGE.encode())
            data = s.recv(BUFFER_SIZE)
            print("Received data:", data.decode())
            time.sleep(DELAY)
        s.close()

send()