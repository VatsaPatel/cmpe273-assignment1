import socket


UDP_IP = '127.0.0.1'

UDP_PORT = 4000
BUFFER_SIZE = 65565
MESSAGE = "ACK Handshake"

Clients = {
    55423 : {
        'fileName1': 'example.txt',
        'fileSize': '',
        'PacketSize': '',
        'Packets': '',
        'Checksum': ''
    }
}

IncomingPackets = {
    55423 : {

    }
}
def listen_forever():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("", UDP_PORT))

    while True:
        # get the data sent to us
        data, ip = s.recvfrom(BUFFER_SIZE)
        print(data.decode(encoding="utf-8").strip())
        data = data.decode(encoding="utf-8").strip()
        s1 = eval(data)
        print(s1['fileName1'])
        #print(ip[1])
        #Clients[ip[1]]
        s.sendto(MESSAGE.encode(), ip)


listen_forever()