import socket
from threading import Thread

BYTES_TO_READ = 4096
HOST = "127.0.0.1"
PORT = 8080

def handle_connection(conn, addr):
	with conn:
		print(f"Connected by: {addr} using port: {conn.getsockname()[1]}")

		while True:
			data = conn.recv(BYTES_TO_READ)
			if not data:
				break
			print(data)
			conn.sendall(data)

def start_server():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.bind((HOST,PORT))
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		s.listen()

		conn, addr = s.accept()
		# Uncomment line 28 and comment out lines 30-33 for single-threaded
		# functionality.
		# handle_connection(conn, addr)

		while True:
			conn, addr = s.accept()
			thread = Thread(target=handle_connection, args=(conn, addr))
			thread.run()

start_server()