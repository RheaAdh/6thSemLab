import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp_host = socket.gethostname()
udp_port = 12345
listeningAddress = (udp_host, udp_port)
sock.bind((udp_host, udp_port))
s_name,addr = sock.recvfrom(1024)
s_name = s_name.decode()
print(s_name, "has connected to the chat room\nEnter ctrl+c to exit chat room\n")
name = input(str("Enter your name: "))
sock.sendto(name.encode(),addr)
while True:
    message = input(str("Me : "))
    sock.sendto(message.encode(),addr)
    message,addr = sock.recvfrom(1024)
    message = message.decode()
    print(s_name, ":", message)