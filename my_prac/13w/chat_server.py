import socket
import threading

PORT = 2500
BUFSIZE = 1024

clients = []
clients_lock = threading.Lock()


def broadcast_message(message, sender_client):
    clients_lock.acquire()
    try:
        for client_socket in clients:
            if client_socket != sender_client:
                try:
                    client_socket.send(message.encode())
                except:
                    if client_socket in clients:
                        clients.remove(client_socket)
    finally:
        clients_lock.release()


def handle_client(client_socket, address):
    print("[연결됨] " + str(address[0]) + ":" + str(address[1]))
    
    try:
        while True:
            data = client_socket.recv(BUFSIZE)
            if not data:
                break
            message = data.decode()
            print("[" + str(address[0]) + ":" + str(address[1]) + "] " + message)
            msg = "[" + str(address[0]) + ":" + str(address[1]) + "] " + message
            broadcast_message(msg, client_socket)
    except:
        pass
    
    clients_lock.acquire()
    if client_socket in clients:
        clients.remove(client_socket)
    clients_lock.release()
    
    client_socket.close()


if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', PORT))
    server_socket.listen(5)
    print("서버 시작: [localhost:" + str(PORT) + "]")
    
    try:
        while True:
            client_socket, address = server_socket.accept()
            clients_lock.acquire()
            clients.append(client_socket)
            clients_lock.release()
            
            thread = threading.Thread(target=handle_client, args=(client_socket, address))
            thread.start()
    except:
        pass
    finally:
        for client in clients:
            try:
                client.close()
            except:
                pass
        server_socket.close()
