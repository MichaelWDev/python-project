import socket

HEADER = 64
PORT   = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR   = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

# Sends message to server.py
def send(msg):
	message     = msg.encode(FORMAT)
	msg_length  = len(message)
	send_length = str(msg_length).encode(FORMAT)
	send_length += b' ' * (HEADER - len(send_length)) # Byte representation of string.
	client.send(send_length)
	client.send(message)
	print(client.recv(2048).decode(FORMAT)) # Decodes from byte format.

send("Hello World!") # Sends message (data) to server.
send(DISCONNECT_MESSAGE) # Disconnects user from server.