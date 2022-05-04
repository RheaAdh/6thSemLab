import socket
host = 'localhost'
port = 16008

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)

print("TCP server has started and is ready to receive")

while 1:
    connection, addr = s.accept()
    data = connection.recv(1024)
    if not data: break

    temp = [float(x) for x in data.split()]
    print("Received data:", temp)

    length = len(temp)
    maximum = max(temp)
    minimum = min(temp)
    total = sum(temp)
    mean = total/length

    msg = str(total) + " " + str(minimum) + " " + str(maximum) + " " + str(mean)

    connection.send(str(msg).encode())