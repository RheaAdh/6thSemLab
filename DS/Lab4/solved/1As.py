import socket
HOST = '127.0.0.1' # Standard loopback interface address (localhost)
PORT = 2058
# Port to listen on (non-privileged ports are > 1023)
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
print("binded host to port - server")

s.listen()

print("listening.... - server")
conn, addr = s.accept()

print('Connected by', addr)

data = conn.recv(1024)
print('data',data)
# print("bytedataarr",bytearray(data, 'utf-8'))
print("Client says: ",data.decode())

data = input("Enter message to client:")
# sending message as bytes to client.
conn.sendall(bytearray(data, 'utf-8'))

conn.close()