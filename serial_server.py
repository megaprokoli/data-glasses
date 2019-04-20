import pickle
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 5300))

print("running")

server.listen(0)
client, addr = server.accept()

resp = client.makefile(mode="rb", buffering=1024)

obj = pickle.load(resp)

print(obj)
