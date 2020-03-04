import socket, os, hashlib

UDP_IP = '127.0.0.1'
UDP_PORT = 4000
BUFFER_SIZE = 65565
MESSAGE = "ping"
# MESSAGE = "A" * 65500
data = ''

CHUNK_SIZE = 6550
chunk_lookup = {}
fileName = 'upload.txt'
i = 0

with open(fileName, 'rb+') as ifile:
    while True:
        chunk = ifile.read(CHUNK_SIZE)
        if not chunk: break
        i += 1
        chunk_lookup[i] = chunk

Packets = list(chunk_lookup.keys())[-1]

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
        "Packets": Packets,
        "Checksum": checksum(fileName)
    }


# Handshake_message = f"Sending {Packets} of {CHUNK_SIZE}"
# def send(id=0):
#     try:
#         s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#         s.sendto(str(metadata).encode(), (UDP_IP, UDP_PORT))
#         data, ip = s.recvfrom(BUFFER_SIZE)
#         print(data.decode())
#     except socket.error:
#         print("Error! {}".format(socket.error))
#         exit()
#
#
# send(id=1)
