import Adafruit_SSD1306


class Oled:
    def __init__(self, drawer):
        self.disp = Adafruit_SSD1306.SSD1306_128_32(rst=None)
        self.__draw_strategy = drawer

        self.disp.begin()
        self.disp.clear()
        self.disp.display()

    def draw(self):
        pass

    def set_draw_strategy(self, drawer):
        self.__draw_strategy = drawer
