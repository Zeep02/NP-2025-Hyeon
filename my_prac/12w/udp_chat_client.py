# udp_chat_client.py
# 1:1 UDP 채팅 클라이언트 (Python)

import socket
import sys

BUFFSIZE = 1024

server_ip = input("Server IP (default: localhost): ").strip()
if server_ip == "":
    server_ip = "localhost"

PORT = 2500
server_addr = (server_ip, PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(f"Connected to {server_ip}:{PORT}")
print("Type 'quit' or 'exit' to disconnect")

try:
    while True:
        msg = input("-> ")
        
        if msg.lower() in ["quit", "exit"]:
            print("Disconnecting...")
            break
        
        if not msg.strip():
            continue
        
        sock.sendto(msg.encode(), server_addr)

        print("<- ", end="", flush=True)
        data, addr = sock.recvfrom(BUFFSIZE)
        print(data.decode())

except KeyboardInterrupt:
    print("\nInterrupted by user")
except socket.error as e:
    print(f"Socket error: {e}")
except Exception as e:
    print(f"Error: {e}")
finally:
    sock.close()
    print("Connection closed")