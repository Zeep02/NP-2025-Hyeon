# 객체지향 확장
# 역할 인자에 따라 서버, 클라이언트 구분
import argparse
import socket
from datetime import datetime

BUFFSIZE = 2048


class UDPServer:
    def __init__(self, port: int) -> None:
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(("localhost", port))

    def run(self) -> None:
        print("{}에서대기중...".format(self.sock.getsockname()))
        while True:
            data, address = self.sock.recvfrom(BUFFSIZE)
            text = data.decode("utf-8")
            print("{} 클라이언트메시지{!r}".format(address, text))
            text = "데이터의길이는{} 바이트임".format(len(data))
            self.sock.sendto(text.encode("utf-8"), address)


class UDPClient:
    def __init__(self, port: int) -> None:
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def run(self) -> None:
        text = "현재시각은{}입니다".format(datetime.now())
        data = text.encode("utf-8")
        self.sock.sendto(data, ("localhost", self.port))
        print("운영체제로부터할당받은주소는{}입니다".format(self.sock.getsockname()))
        data, address = self.sock.recvfrom(BUFFSIZE)
        text = data.decode("utf-8")
        print("서버{}의응답은{!r}입니다".format(address, text))


if __name__ == "__main__":
    mode = {"c": UDPClient, "s": UDPServer}
    parser = argparse.ArgumentParser(description="Send and receive UDP locally")
    parser.add_argument("role", choices=["c", "s"], help="which role to play")
    parser.add_argument(
        "-p",
        metavar="PORT",
        type=int,
        default=2500,
        help="UDP port (default 2500)",
    )
    args = parser.parse_args()
    operation = mode[args.role](args.p)
    operation.run()

