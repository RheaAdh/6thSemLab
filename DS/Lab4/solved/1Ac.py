import socket
HOST = '127.0.0.1' # The server's hostname or IP address
PORT = 2058
# The port used by the server
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("connecting... - client")
s.connect((HOST, PORT))
print("connected... - client")

s.sendall(b'Im client')

data = s.recv(1024)

print('Server says:', data.decode())