# Charith Pathirathna
# Lab 02
# References: https://github.com/aianta/cmput404-tcp-lab from Lab Session.

import socket

BYTES_TO_READ = 4096

def get(host, port):
	# create request
	request_data = b"GET / HTTP/1.1\nHost:" + host.encode('utf-8') + b"\n\n"

	# create socket
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# send data
	s.connect((host, port))
	s.send(request_data)
	s.shutdown(socket.SHUT_WR)

	# listen and print response to console
	response = s.recv(BYTES_TO_READ)
	while(len(response) > 0):
		print(response)
		response = s.recv(BYTES_TO_READ)

	s.close()

print("www.google.com", 80)