# server.py
import socket
import time
host = socket.gethostname()
port = 9991
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(5)
conn,addr = s.accept()
print("Got a connection from %s" % str(addr))
currentTime = time.ctime(time.time()) + "\r\n"
print(currentTime)
conn.send(currentTime.encode('ascii'))
conn.close()