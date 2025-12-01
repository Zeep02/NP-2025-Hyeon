import java.io.*;
import java.net.*;
import java.util.*;

public class ChatServer {
    private static final int PORT = 2500;
    private static List<Socket> clients = new ArrayList<>();
    
    public static void main(String[] args) {
        ServerSocket serverSocket = null;
        try {
            serverSocket = new ServerSocket(PORT);
            System.out.println("서버 시작: [localhost:" + PORT + "]");
            
            while (true) {
                Socket clientSocket = serverSocket.accept();
                
                synchronized (clients) {
                    clients.add(clientSocket);
                }
                
                Thread thread = new Thread(new ClientHandler(clientSocket));
                thread.start();
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (serverSocket != null) {
                try {
                    serverSocket.close();
                } catch (IOException e) {
                }
            }
        }
    }
    
    public static void broadcastMessage(String message, Socket senderSocket) {
        synchronized (clients) {
            for (Socket clientSocket : clients) {
                if (clientSocket != senderSocket) {
                    try {
                        if (!clientSocket.isClosed()) {
                            PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true);
                            out.println(message);
                        }
                    } catch (IOException e) {
                        clients.remove(clientSocket);
                    }
                }
            }
        }
    }
    
    static class ClientHandler implements Runnable {
        private Socket clientSocket;
        private String address;
        
        public ClientHandler(Socket socket) {
            this.clientSocket = socket;
            this.address = socket.getInetAddress().getHostAddress() + ":" + socket.getPort();
        }
        
        public void run() {
            System.out.println("[연결됨] " + address);
            try {
                BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
                String message;
                while ((message = in.readLine()) != null) {
                    System.out.println("[" + address + "] " + message);
                    broadcastMessage("[" + address + "] " + message, clientSocket);
                }
            } catch (IOException e) {
            } finally {
                synchronized (clients) {
                    clients.remove(clientSocket);
                }
                try {
                    clientSocket.close();
                } catch (IOException e) {
                }
            }
        }
    }
}
