# 연습문제 1-1
import telnetlib


HOST = "localhost"
PORT = 5000

with telnetlib.Telnet(HOST, PORT, timeout=5) as tn:
    response = tn.read_all()
    print(response.decode("utf-8", errors="replace"))


