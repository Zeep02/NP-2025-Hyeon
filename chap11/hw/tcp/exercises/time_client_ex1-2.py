# 연습문제 1-2
import socket
import time


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 5000))
raw = sock.recv(1024).decode()
parsed = time.strptime(raw)
formatted = time.strftime("%Y %b %d (%a) %H:%M:%S", parsed)
print(formatted)


