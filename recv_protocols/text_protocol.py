from recv_protocols.recv_protocol import RecvProtocol


class TextProtocol(RecvProtocol):
    def __init__(self, socket, client_addr):
        super().__init__(socket, client_addr)

    def receive(self, content_len):
        content = self._socket.recv(content_len)

        return content
