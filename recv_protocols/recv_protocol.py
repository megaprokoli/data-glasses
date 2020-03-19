from abc import ABC
from abc import abstractmethod


class RecvProtocol(ABC):
    def __init__(self, socket, client_addr):
        self._socket = socket
        self._addr = client_addr

    @abstractmethod
    def receive(self, content_len):
        pass
