import socket 
import datetime
from dateutil import parser
from timeit import default_timer as timer 

host='localhost'
port=12346

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)


s.connect((host,port))


starttime=timer()

servertime=parser.parse(s.recv(1024).decode())

response_time=timer()


latency=response_time-starttime

clienttime=servertime+datetime.timedelta(latency)/2


currtime=datetime.datetime.now()

err=currtime-clienttime

print("err:"+str(err))
print("curr"+str(currtime))

