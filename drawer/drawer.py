from abc import ABC
from abc import abstractmethod


class Drawer(ABC):
    def __init__(self, content=None):
        self._content = content

    @abstractmethod
    def draw(self, disp):
        pass
