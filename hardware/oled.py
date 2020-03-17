import adafruit_ssd1306


class Oled:
    def __init__(self, drawer):
        self.disp = adafruit_ssd1306.SSD1306_128_32(rst=None)
        self.__draw_strategy = drawer

        self.disp.begin()
        self.disp.clear()
        self.disp.display()

    def draw(self):
        self.__draw_strategy.draw(self.disp)

    def set_draw_strategy(self, drawer):
        self.__draw_strategy = drawer
