from hardware.oled import Oled
from server.bluetooth_server import BluetoothServer
from content.content_api import ContentAPI


oled = Oled(drawer=ContentAPI.get_content_type("text").drawer("started v0.2"))  # TODO improve
server = BluetoothServer("127.0.0.1", 5300)  # TODO set ip and port in constr

server.start()
oled.draw()

print("running")

s_gen = server.run_gen()

while True:

    if not server.running:
        break

    for drawer in s_gen:
        oled.set_draw_strategy(drawer)
        oled.draw()
