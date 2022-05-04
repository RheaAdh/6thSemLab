#client.py
import socket
host = socket.gethostname()
port = 9991
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
tm = s.recv(1024)
print(tm)
print(' Current time from Sever :', tm.decode())
s.close()