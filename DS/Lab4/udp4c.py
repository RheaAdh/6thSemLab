import socket

host = 'localhost'
port = 16008

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = input("Input integers with space in between: ")
message2 = input("Enter the length of the set: ")

s.sendto(message.encode(),(host,port))
s.sendto(message2.encode(),(host,port))

data,addr = s.recvfrom(1024)

temp = [float(x) for x in data.split()]

print("The total of all numbers is: " + str(temp[0]))
print("The lowest number is: " + str(temp[1]))
print("The highest number is: " + str(temp[2]))
print("The mean is: " + str(temp[3]))