import socket 
import datetime

host='localhost'
port=12346

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((host,port))

s.listen(5)

conn,addr=s.accept()
conn.send(str(datetime.datetime.now()).encode())

s.close()