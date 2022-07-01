import socket
import threading

FORMAT = 'utf-8'
HEADER = 64
PORT = 8080
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
EXIT = "!exit"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
print(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == EXIT:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("OLHA DE VOLTA".encode(FORMAT))

    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[CONECÇÕES ATIVAS] {threading.activeCount() - 1}")

print("INICIANDO......")
start()


