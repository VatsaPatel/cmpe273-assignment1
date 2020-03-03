import socket, os, hashlib, sys
from typing import Dict

UDP_IP = '127.0.0.1'
UDP_PORT = 4000
BUFFER_SIZE = 65565
MESSAGE = "ping"
data = ''
RETRY_LIMIT = 3
CHUNK_SIZE = 60000
chunk_lookup: Dict[int, bytes] = {}
fileName = sys.argv[1]
i = 0

with open(fileName, 'rb+') as ifile:
    while True:
        chunk = ifile.read(CHUNK_SIZE)
        if not chunk: break
        i += 1
        chunk_lookup[i] = chunk

def checksum(fileName):
    with open("upload.txt", "rb") as f:
        file_hash = hashlib.md5()
        while chunk := f.read(8192):
            file_hash.update(chunk)
    return file_hash.hexdigest()

metadata = {
        "fileName": fileName,
        "fileSize": os.path.getsize(fileName),
        "PacketSize": CHUNK_SIZE,
        "Packets": chunk_lookup.__len__(),
        "Checksum": checksum(fileName)
    }

def retry(s,x):
    for i in range(RETRY_LIMIT):
        print('Retry no.:', i)
        s.sendto(str(f'/~{x};!^@').encode() + chunk_lookup[x], (UDP_IP, UDP_PORT))
        data, ip = s.recvfrom(BUFFER_SIZE)
        t = int(data.split(b'|^', 1)[1].decode())
        # print('retry is:',t)
        if t == x:
            return 0
    print("Aborting upload. Please try again")
    quit()

def StartSending(s):
    for x in range(1, chunk_lookup.__len__() + 1):
        s.sendto(str(f'/~{x};!^@').encode()+chunk_lookup[x], (UDP_IP, UDP_PORT))
        data, ip = s.recvfrom(BUFFER_SIZE)
        t = int(data.split(b'|^', 1)[1].decode())
        print('Received ACK for Packet no.',t)
        if t != x:
           retry(s,x)


def send():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto(str(metadata).encode(), (UDP_IP, UDP_PORT))
        data, ip = s.recvfrom(BUFFER_SIZE)
        if data.decode() == 'ACK Handshake':
            print("Connected to Server and Handshake complete")
            print(f"Strating file ({metadata['fileName']}) upload.", )
            StartSending(s)
            s.sendto("Payload Done!!".encode(), (UDP_IP, UDP_PORT))
            data, ip = s.recvfrom(BUFFER_SIZE)
            print(data.decode())

    except socket.error:
        print("Error! {}".format(socket.error))
        exit()

send()
