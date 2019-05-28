import socket

# packet structure
# header 96b
# 32b drawer_id | 64b content len | content

id = "text"
header = "{:<32}{:<64}".format(id, len(id)).encode()
content = b'stop'
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(header)

c.connect(("127.0.0.1", 5300))


c.send(header)
c.recv(1024)
c.send(content)

c.close()

print("sent")
