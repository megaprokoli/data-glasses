from hardware.oled import Oled
from server.bluetooth_server import BluetoothServer
from content.content_api import ContentAPI
import specs


oled = Oled(drawer=ContentAPI.get_content_type("text").drawer("started v0.2"))  # TODO improve
server = BluetoothServer("192.168.2.121", 5300, verbose=True)

# SET SPECS
specs.DISP_DIMENSIONS = (oled.disp.width, oled.disp.height)

server.start()
oled.draw()

print("running")

s_gen = server.run_gen()

while True:

    if not server.running:
        break

    for drawer in s_gen:
        # print(drawer)
        oled.set_draw_strategy(drawer)
        oled.draw()

# TODO cleanup display on exit
