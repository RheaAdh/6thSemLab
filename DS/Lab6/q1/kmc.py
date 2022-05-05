from timeit import default_timer as timer
from dateutil import parser
import threading
import datetime
import socket
import time

def startSendingTime(s):
	while True:
		s.send(str(datetime.datetime.now()).encode())
		print("KMC time sent successfully", end = "\n\n")
		time.sleep(5)

def startReceivingTime(s):
	while True:
		Synchronized_time = parser.parse(s.recv(1024).decode())
		print("Synchronized time at the client is: " + str(Synchronized_time), end = "\n\n")

def initiateSlaveClient(port = 8080):
	s = socket.socket()
	s.connect(('127.0.0.1', port))
	print("Starting to receive time from server\n")
	send_time_thread = threading.Thread(
		target = startSendingTime,
		args = (s, ))
	send_time_thread.start()
	print("Starting to recieving synchronized time from server\n")
	receive_time_thread = threading.Thread(
		target = startReceivingTime,
		args = (s, ))
	receive_time_thread.start()

if __name__ == '__main__':
	initiateSlaveClient(port = 8080)