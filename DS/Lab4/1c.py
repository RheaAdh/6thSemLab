import socket
encmsg = str.encode("HelloUDP Server")
addr_port = ("127.0.0.1", 20001)
bufferSize = 1024
# Create a UDP socket at client side
s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Send to server using created UDP socket
s.sendto(encmsg, addr_port)
msgFromServer = s.recvfrom(bufferSize)
msg = "Message from Server {}".format(msgFromServer[0])
print(msg)