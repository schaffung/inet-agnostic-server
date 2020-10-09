import socket
import socketserver
import threading

# Subclass so that IPv4 packets are captured.
class UDPServer4(socketserver.ThreadingUDPServer):
    address_family = socket.AF_INET

# Subclass so that IPv6 packets are captured.
class UDPServer6(socketserver.ThreadingUDPServer):
    address_family = socket.AF_INET6

class MainPackethandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = self.request[0].strip()
        print(data)

def UDP_server_thread(sock):
    sock.serve_forever()

server4 = UDPServer4(("0.0.0.0", 21000), MainPackethandler)
server6 = UDPServer6(("::1", 21000), MainPackethandler)

server_thread1 = threading.Thread(target=UDP_server_thread, args=(server4,))
server_thread2 = threading.Thread(target=UDP_server_thread, args=(server6,))

server_thread1.start()
server_thread2.start()


