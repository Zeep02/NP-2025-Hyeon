import socket
import threading

PORT = 2500
BUFSIZE = 1024

client_socket = None
running = True


def receive_messages():
    global running
    while running:
        try:
            data = client_socket.recv(BUFSIZE)
            if not data:
                break
            print(data.decode())
        except:
            break
    running = False


if __name__ == "__main__":
    server_ip = input("Server IP (default: localhost): ").strip()
    if server_ip == "":
        server_ip = "localhost"
    
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_ip, PORT))
        print("서버 연결: [" + server_ip + ":" + str(PORT) + "]")
        
        thread = threading.Thread(target=receive_messages)
        thread.start()
        
        while True:
            message = input()
            client_socket.send(message.encode())
    except:
        print("오류 발생")
    finally:
        running = False
        if client_socket:
            client_socket.close()
