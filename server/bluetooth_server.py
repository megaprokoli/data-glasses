import socket
from recv_protocols.recv_protocol import RecvProtocol
from content.content_api import ContentAPI


class BluetoothServer:  # TODO bluetooth
    def __init__(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._protocol = None
        self.running = False

        self._socket.bind(("127.0.0.1", 5300))

    def _read_header(self, client):
        # packet structure
        # header 96b
        # 32b drawer_id | 64b content len | content

        drawer_id = client.recv(32).decode()
        content_len = int(client.recv(64).decode())
        client.send(b'ack')

        drawer_id = drawer_id.replace(" ", "")  # remove padding whitespaces

        return drawer_id, content_len

    def start(self):
        self.running = True

    def stop(self):
        self.running = False

    def run_gen(self):
        # if not self.initialized:
        #     self.stop()
        #     # TODO raise exception
        #     return

        while self.running:
            self._socket.listen(0)
            client, addr = self._socket.accept()

            header = self._read_header(client)
            content_type = ContentAPI.get_content_type(header[0])
            proto = content_type.protocol(client, addr)
            content = proto.receive(header[1])

            yield content_type.drawer(content)
        return

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
