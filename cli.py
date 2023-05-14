import threading
import socket

client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
client.connect(("b4:8c:9d:ad:ea:c8", 4))

while True:
    data = client.recv(1024)
    print(f"Message: {data.decode('utf-8')}")