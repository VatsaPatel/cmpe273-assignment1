# Assignment 1 - Part B 

UDP Server

## Features
* Support for any file type.
* Connection handshake with all file metadata for checksum verification.
* ACK for each packet. With retry limit of 10 or abort.
* File reconstruction if packet comes out of order.

## Usage
* Make sure to have highest MTU for no packet fragmentation.


* UDP Server

```
python3 udp_server.py

Server started at port 4000.
Accepting a file upload...
Upload successfully completed.
```

* UDP Client

```
python3 udp_client.py [Filename]

Connected to the server.
Starting a file {FileName) upload...
Received ack(xxxxxx) from the server.
Received ack(xxxxxx) from the server.
.
..
File upload successfully completed.
```