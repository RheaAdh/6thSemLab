import socket
import datetime
import time

s=socket.socket()
print("Socket successfully created")
host='localhost'
port=8011
s.bind((host,port))
s.listen(5)
print("Socket is listening...")

conn,addr=s.accept()
print("server connected to ",addr)
conn.send(str(datetime.datetime.now()).encode())
conn.close()