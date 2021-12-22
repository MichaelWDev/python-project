import socket
import threading

HEADER = 64
PORT   = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR   = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
	print(f"[NEW CONNECTION] {addr} connected.")

	connected = True
	while connected:
		msg_length = conn.recv(HEADER).decode(FORMAT)
		
		if msg_length:
			msg_length = int(msg_length)
			msg = conn.recv(msg_length).decode(FORMAT)

			if msg == DISCONNECT_MESSAGE:
				connected = False

			print(f"[{addr}] {msg}")
			conn.send("[RECEIVED] Message received.".encode(FORMAT))

	conn.close()

def start():
	server.listen()
	print(f"[LISTENING] Server is listening on {SERVER}")
	while True:
		conn, addr = server.accept()
		thread = threading.Thread(target=handle_client, args=(conn, addr))
		thread.start()
		print(f"[ACTIVE CONNECTIONS {threading.activeCount() - 1}")


print("[STARTING] Server is starting...")
start()




"""
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Allows user to connect from any IP to port 1500.
sock.bind(('0.0.0.0', 1500))

sock.listen(1)

connections = []

def handler(c, a):
	global connections # Allows access to the connections list above.
	while True:
		data = c.recv(1024) # 1024 bytes
		for connection in connections:
			connection.send(bytes(data)) # Converts data from string to bytes.
		if not data:
			connections.remove(c)
			c.close()
			break

while True:
	c, a = sock.accept()
	cThread = threading.Thread(target=handler, args=(c, a))
	cThread.daemon = True # You can close your program regardless of anything.
	cThread.start()
	connections.append(c)
	print(connections)
"""