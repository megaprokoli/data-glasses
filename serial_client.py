import socket

# packet structure
# header 96b
# 32b drawer_id | 64b content len | content


def build_header(id, content):
    return "{:<32}{:<64}".format(id, len(content)).encode()


inp = input("Enter content: ")

while inp != "stop":
    header = build_header("text", inp)

    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect(("192.168.2.121", 5300))

    c.send(header)
    c.recv(1024)
    c.send(inp.encode())

    c.close()

    print("sent")

    inp = input("Enter content: ")

print("Good Bye")
