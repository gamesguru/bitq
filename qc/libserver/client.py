import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("69.14.146.157", 8333))
client.send(b"I am CLIENT<br>")
from_server = client.recv(4096)
client.close()
print(from_server.decode())
