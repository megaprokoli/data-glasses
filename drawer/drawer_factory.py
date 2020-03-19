from drawer.text_drawer import TextDrawer
from drawer.animation_drawer import AnimationDrawer
from drawer.image_drawer import ImageDrawer

# DEPRECATED

class DrawerFactory:
    def __init__(self):
        self._strategy_map = {"text": TextDrawer,
                              "image": ImageDrawer,
                              "animation": AnimationDrawer}

    def get_instance(self, drawer_id, content):
        try:
            return self._strategy_map[drawer_id](content)
        except KeyError:
            return None
