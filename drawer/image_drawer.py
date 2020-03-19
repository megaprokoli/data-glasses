import pickle

from drawer.drawer import Drawer


class ImageDrawer(Drawer):
    def __init__(self, content):
        super().__init__(content)

    def draw(self, disp):
        img = pickle.loads(self._content)

        disp.clear()
        disp.display()

        disp.image(img)
        disp.display()
