import socket
import string
import threading

FORMAT = 'utf-8'
HEADER = 64
PORT = 8080
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
EXIT = "exit"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
print(ADDR)

def f1(conn):
    conn.send("Entre com o nome:".encode(FORMAT))
    nome = read(conn)
    conn.send("Entre com o cargo:".encode(FORMAT))
    cargo = read(conn).lower()
    conn.send("Entre com o salario:".encode(FORMAT))
    salario = float(read(conn))

    if cargo == "operador":
        salario *= 1.2
    else: 
        salario *= 1.18

    saida = "\n{}\nR$ {}\n\nEntre com o némero função entre 1 e 9 ou \"exit\" para sair"
    saida = saida.format(nome, salario)
    #print(saida)
    return saida

def f2(conn):
    pass

def f3(conn):
    pass

def f4(conn):
    pass

def f5(conn):
    pass

def f6(conn):
    pass

def f7(conn):
    pass

def f8(conn):
    pass

def f9(conn):
    pass


def read(conn):
    msg_length = conn.recv(HEADER).decode(FORMAT)
    msg_length = int(msg_length)
    msg = conn.recv(msg_length).decode(FORMAT)
    return msg

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    conn.send("Entre com o némero função entre 1 e 9 ou \"exit\" para sair".encode(FORMAT))
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == EXIT:
                connected = False
                conn.send("[DISCONNECTING...]".encode(FORMAT))
            else:
                if int(msg) == 1:
                    print("é 1")
                    conn.send(f1(conn).encode(FORMAT))

                if int(msg) == 2:
                    print("é 2")
                    conn.send("é 2".encode(FORMAT))
                if int(msg) == 3:
                    print("é 3")
                if int(msg) == 4:
                    print("é 4")
                if int(msg) == 5:
                    print("é 5")
                if int(msg) == 6:
                    print("é 6")
                if int(msg) == 7:
                    print("é 7")
                if int(msg) == 8:
                    print("é 8")
                if int(msg) == 9:
                    print("é 9")

            #print(f"[{addr}] {msg}")
            #conn.send("OLHA DE VOLTA".encode(FORMAT))

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


