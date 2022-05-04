import socket
host = 'localhost'
port = 16008

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))

print("TCP server has started and is ready to receive")

while 1:
    data, addr = s.recvfrom(1024)
    if not data: 
        break

    temp = [float(x) for x in data.split()]
    print("Received data:", temp)

    length = len(temp)
    maximum = max(temp)
    minimum = min(temp)
    total = sum(temp)
    mean = total/length

    msg = str(total) + " " + str(minimum) + " " + str(maximum) + " " + str(mean)

    s.sendto(str(msg).encode(),addr)