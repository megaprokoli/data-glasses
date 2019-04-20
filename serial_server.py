import pickle
import socket

from drawer.text_drawer import TextDrawer
from hardware.oled import Oled


oled = Oled(drawer=TextDrawer("started"))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 5300))

print("running")

while True:
    server.listen(0)
    client, addr = server.accept()

    resp = client.makefile(mode="rb", buffering=1024)

    obj = pickle.load(resp)

    print(obj)
