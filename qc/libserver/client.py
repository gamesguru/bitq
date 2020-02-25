import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("69.14.146.157", 8333))
data = open('wolfram-alpha-1.4.1.apk', 'rb').read()
client.send(data)
from_server = client.recv(4096)
client.close()
print(from_server.decode())
