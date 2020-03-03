import socket

UDP_IP = '127.0.0.1'

UDP_PORT = 4000
BUFFER_SIZE = 65565

Clients = {
}

IncomingPackets = {
}

def merger(port):
    with open(f"Uploads/{Clients[port]['fileName']}", 'wb+') as ifile:
        for x in range(1,Clients[port]['Packets']+1):
            ifile.write(bytes(IncomingPackets[port][x]))

def Storer(s,dataB,ip):
    t = dataB.split(b';', 1)
    key = int(t[0].split(b'/~', 1)[1])
    val = t[1].split(b'!^@', 1)[1]
    q = {key: val}
    IncomingPackets[ip[1]].update(q)
    s.sendto(f"|^{str(key)}".encode(), ip)

def listen_forever():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("", UDP_PORT))
    print(f"Server started at port {UDP_PORT}.")
    while True:
        # get the data sent to us
        dataB, ip = s.recvfrom(BUFFER_SIZE)
        # print(dataB)
        if dataB.startswith(b"{'fileName'"):
            data = dataB.decode()
            Clients[ip[1]] = eval(data)
            IncomingPackets[ip[1]]: Dict[int, bytes] = {}
            s.sendto("ACK Handshake".encode(), ip)
            print("Accepting a file upload...")
        elif dataB.startswith(b'/~'):
            Storer(s,dataB,ip)
        elif dataB == b'Payload Done!!':
            merger(port = ip[1])
            s.sendto("Upload Successful!".encode(), ip)
            print("Upload successfully completed.")
        else:
            print('Wrong incoming Data!!')

listen_forever()
