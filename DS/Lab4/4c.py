import socket

host = 'localhost'
port = 16008

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

message = input("Input integers with space in between: ")
message2 = input("Enter the length of the set: ")

s.send(message.encode())
s.send(message2.encode())

data = s.recv(1024)
print(data)
for x in data.split():
    print(x)
temp = [float(x) for x in data.split()]
print(temp)
print("The total of all numbers is: " + str(temp[0]))
print("The lowest number is: " + str(temp[1]))
print("The highest number is: " + str(temp[2]))
print("The mean is: " + str(temp[3]))

s.close()