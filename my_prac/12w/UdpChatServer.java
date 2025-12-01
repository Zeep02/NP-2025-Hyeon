// UdpChatServer.java
// 1:1 UDP 채팅 서버 (Java)

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.util.Scanner;

public class UdpChatServer {
    private static final int PORT = 2500;
    private static final int BUFSIZE = 1024;

    public static void main(String[] args) {

        System.out.println("# 1:1 UDP Chat Server (Java)");
        System.out.println("Listening on port " + PORT);

        try (DatagramSocket socket = new DatagramSocket(PORT)) {

            byte[] buffer = new byte[BUFSIZE];
            Scanner scanner = new Scanner(System.in);

            while (true) {
                // 수신
                DatagramPacket recvPacket = new DatagramPacket(buffer, buffer.length);
                socket.receive(recvPacket);

                String msg = new String(recvPacket.getData(), 0, recvPacket.getLength(), "UTF-8");
                InetAddress clientIp = recvPacket.getAddress();
                int clientPort = recvPacket.getPort();

                System.out.print("<- ");
                System.out.println(msg);

                // 송신
                System.out.print("-> ");
                String response = scanner.nextLine();

                byte[] sendBytes = response.getBytes("UTF-8");
                DatagramPacket sendPacket =
                        new DatagramPacket(sendBytes, sendBytes.length, clientIp, clientPort);
                socket.send(sendPacket);
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}