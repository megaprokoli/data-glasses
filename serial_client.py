import pickle
import socket

example = {1: "2", 2: "hi"}

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(("127.0.0.1", 5300))

transf_file = c.makefile(mode="wb", buffering=1024)
pickle.dump(example, transf_file, pickle.HIGHEST_PROTOCOL)

c.close()

print("sent")
