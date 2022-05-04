import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host='localhost'
port=12347
s.bind((host,port))


data,addr=s.recvfrom(1024)

temp=[float (x) for x in data.split()]

print(temp)


length=len(temp)
mx=max(temp)
mn=min(temp)
tot=sum(temp)

mean=tot/length

msg=str(tot)+" "+str(mn)+" "+str(mx)+" "+str(mean)

s.sendto(str(msg).encode(),addr)