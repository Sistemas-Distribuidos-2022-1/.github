from http import client
import socket

FORMAT = 'utf-8'
HEADER = 64
PORT = 8080
EXIT = "exit"

SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    #print(f"[SENDING]: {msg}")
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    #print(client.recv(2048).decode(FORMAT))


print(client.recv(2048).decode(FORMAT))
run = True
while(run):
    msg = input()
    send (msg)
    print(client.recv(2048).decode(FORMAT))
    if msg == EXIT:
        run = False
