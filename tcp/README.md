# Assignment 1 - Part A TCP

## Features

* Multithreaded Server
* Support for multiple clients at same time.
* Connection start and connection close detection with Client id.

## Usage

* TCP Server


```
python3 tcp_client.py [client id] [delay in seconds between messages] [number of 'ping' messages]
```

```
python3 tcp_server.py
Server started at port 5000.
Connected Client:A.
Received data:A:ping
Connected Client:B.
Received data:B:ping
Received data:A:ping
Received data:B:ping
Received data:A:ping
Received data:B:ping
...
```

* Client A

```
python3 tcp_client.py A 10 3
Sending data:ping
Recevied data:pong
Sending data:ping
Recevied data:pong
Sending data:ping
Recevied data:pong
```

* Client B

```
python3 tcp_client.py B 10 5
Sending data:ping
Recevied data:pong
Sending data:ping
Recevied data:pong
Sending data:ping
Recevied data:pong
Sending data:ping
Recevied data:pong
Sending data:ping
Recevied data:pong
```