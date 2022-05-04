import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp_host = '172.16.58.157'
udp_port = 12345
name = input(str("\nEnter your name: "))
sock.sendto(name.encode(), (udp_host,udp_port));
s_name,addr = sock.recvfrom(1024)
s_name = s_name.decode()
print(s_name, "has joined the chat room\nEnter ctrl+c to exit chat room\n")
while True:
    message,addr = sock.recvfrom(1024)
    message = message.decode()
    print(s_name, ":", message)
    message = input(str("Me : "))
    sock.sendto(message.encode(),addr)
