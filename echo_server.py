# Charith Pathirathna
# Lab 02
# References: https://github.com/aianta/cmput404-tcp-lab from Lab Session.

import socket
from threading import Thread

BYTES_TO_READ = 4096
HOST = "127.0.0.1"
PORT = 8080

# Handles all incoming connections
def handle_connection(conn, addr):
	with conn:
		print(f"Connected by: {addr} using port: {conn.getsockname()[1]}")

		while True:
			data = conn.recv(BYTES_TO_READ)
			if not data:
				break
			print(data)
			conn.sendall(data)

# Starts the server using the given HOST and PORT
def start_server():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.bind((HOST,PORT))
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		s.listen()

		conn, addr = s.accept()
		# Uncomment line 34 and comment out lines 36-39 for single-threaded
		# functionality.
		# handle_connection(conn, addr)

		while True:
			conn, addr = s.accept()
			thread = Thread(target=handle_connection, args=(conn, addr))
			thread.run()

start_server()