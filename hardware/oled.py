class Oled:
    def __init__(self, drawer):
        self.__draw_strategy = drawer

    def draw(self):
        pass

    def set_draw_strategy(self, drawer):
        self.__draw_strategy = drawer
