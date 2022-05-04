import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host='127.0.0.1'
port=12346
s.connect((host,port))
msg1=input("enter numbers of arr")

s.send(msg1.encode())

data=s.recv(1024)

for x in data.split():
    print(x)

temp=[float(x) for x in data.split()]

print("The total of all numbers is: " + str(temp[0]))
print("The lowest number is: " + str(temp[1]))
print("The highest number is: " + str(temp[2]))
print("The mean is: " + str(temp[3]))

s.close()