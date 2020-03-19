import socket
import pickle

from recv_protocols.recv_protocol import RecvProtocol
from content.content_api import ContentAPI
import specs


class BluetoothServer:  # TODO bluetooth
    def __init__(self, addr, port, verbose=False):
        self._verbose = verbose
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._protocol = None
        self._server_functions = {"ping": self.__ping,
                                  "types": self.__content_types,
                                  "specs": self.__sys_specs}
        self.running = False

        self._socket.bind((addr, port))

    @property
    def initialized(self):
        if self._protocol is None:
            return False
        return True

    @property
    def recv_protocol(self):
        return self._protocol

    @recv_protocol.setter
    def recv_protocol(self, proto):
        if isinstance(proto, RecvProtocol):
            self._protocol = proto

    def _read_header(self, client):
        # packet structure
        # header 96b
        # 32b drawer_id | 64b content len | content

        drawer_id = client.recv(32).decode()
        content_len = int(client.recv(64).decode())
        client.send(b'ack')

        drawer_id = drawer_id.replace(" ", "")  # remove padding whitespaces

        return drawer_id, content_len

    def __handle_sfunc_request(self, client, obj):
        serialized = pickle.dumps(obj)

        client.send(str(len(serialized)).encode())
        client.recv(3)  # wait for ack
        client.send(serialized)

    def __ping(self, client):   # doesnt need to do anything client uses b'ack' from read header
        pass

    def __sys_specs(self, client):
        sp = specs.DISP_DIMENSIONS
        self.__handle_sfunc_request(client, sp)

    def __content_types(self, client):
        types = ContentAPI.available_content_types()
        self.__handle_sfunc_request(client, types)

    def is_server_func(self, id):
        return id in self._server_functions.keys()

    def start(self):
        self.running = True

    def stop(self):
        self.running = False

    def run_gen(self):
        while self.running:
            self._socket.listen(0)
            client, addr = self._socket.accept()

            header = self._read_header(client)

            if self._verbose:
                print("{} | id: {} length: {}".format(addr, header[0], header[1]))

            if self.is_server_func(header[0]):
                self._server_functions[header[0]](client)
            else:
                content_type = ContentAPI.get_content_type(header[0])
                proto = content_type.protocol(client, addr)
                content = proto.receive(header[1])

                yield content_type.drawer(content)
        return
