import socket
import threading

PORT   = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR   = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    pass

def start():
    server.listen()
    while True:
        conn, addr = server.accept()


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