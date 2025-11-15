# 연습문제 2 - 터미널에서 py dummy_tcp_client_arg.py -p 2500 으로 실행
import argparse
import socket


parser = argparse.ArgumentParser()
parser.add_argument("-s", default="127.0.0.1")
parser.add_argument("-p", type=int, default=2500)
args = parser.parse_args()

address = (args.s, args.p)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(address)

while True:
    msg = input("Message to send: ")
    sock.send(msg.encode())
    data = sock.recv(1024)
    if not data:
        break
    print("Received message: %s" % data.decode())


