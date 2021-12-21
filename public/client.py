import socket

HEADER = 64
PORT   = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR   = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

# 34:05