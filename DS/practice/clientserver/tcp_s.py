import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host='127.0.0.1'
port=12346
s.bind((host,port))
s.listen(5)
conn,addr=s.accept()
data=conn.recv(1024)

temp=[float(x) for x in data.split()]
print ("received data: ",temp)

length=len(temp)
mx=max(temp)
mn=min(temp)
tot=sum(temp)

mean=tot/length

msg=str(tot)+" "+str(mn)+" "+str(mx)+" "+str(mean)

conn.send(str(msg).encode())