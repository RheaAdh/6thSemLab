import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host='localhost'
port=12347

s.connect((host,port))


arr=input("enter numbers of arr")


s.sendto(arr.encode(),(host,port))

data,addr=s.recvfrom(1024)

temp=[float(x) for x in data.split()]

print("The total of all numbers is: " + str(temp[0]))
print("The lowest number is: " + str(temp[1]))
print("The highest number is: " + str(temp[2]))
print("The mean is: " + str(temp[3]))

s.close()