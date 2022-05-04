import socket
s = socket.socket()
host = '127.0.0.1'
port = 11596
print('Waiting for connection')
try:
    s.connect((host, port))
except socket.error as e:
    print(str(e))
Response = s.recv(1024)
while True:
    Input = input('Client Say Something: ')
    s.send(str.encode(Input))
    Response = s.recv(1024)
    print('From Server : ' + Response.decode())
s.close()