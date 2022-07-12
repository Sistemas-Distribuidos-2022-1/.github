import socket
import string
import threading
import random

FORMAT = 'utf-8'
HEADER = 64
PORT = 8080
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
EXIT = "exit"
HELP = "[HELP] Entre com o némero função entre 1 e 9 ou \"exit\" para sair:"

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

    saida = f"\nReajuste de {nome} é R$ {salario}\n\n{HELP}"
    #print(saida)
    return saida
def f2(conn):
    conn.send("Entre com o nome:".encode(FORMAT))
    nome = read(conn)
    conn.send("Entre com o sexo (M ou F):".encode(FORMAT))
    sexo = read(conn).upper()
    conn.send("Entre com a idade:".encode(FORMAT))
    idade = int(read(conn))
    if(idade >= 18 and sexo == "M"):
        saida = f"{nome} é Maior de idade"
    else: 
        if(idade >= 21 and sexo == "F"):
            saida = f"{nome} é Maior de idade"
        else:
            saida = f"{nome} é Menor de idade"
    saida = f"\n{saida}\n{HELP}\n"
    return saida
def f3(conn):
    conn.send("Entre com o N1:".encode(FORMAT))
    N1 = int(read(conn))
    conn.send("Entre com o N2:".encode(FORMAT))
    N2 = int(read(conn))
    if(((N2+N1)/2)>=7):
        saida = f"\nAprovado\n\n{HELP}\n"
        return saida
    else:
        if(((N2+N1)/2)<=3):
            saida = f"\nReprovado\n\n{HELP}\n"
            return saida
        else:
            conn.send("Entre com o N3:".encode(FORMAT))
            N3 = int(read(conn))
            if((((N2+N1)/2)+N3)/2 >=5):
                saida = f"\nAprovado\n\n{HELP}\n"
                return saida
            else:
                saida = f"\nReprovado\n\n{HELP}\n"
                return saida
def f4(conn):
    conn.send("Entre com o sexo (M ou F):".encode(FORMAT))
    sexo = read(conn).upper()
    conn.send("Entre com a altura:".encode(FORMAT))
    altura = float(read(conn))
    if(sexo == "M"):
        saida = (72.7 * altura) - 58
    else:
        saida =  (62.1 * altura) - 44.7
    saida = f"Peso ideal é {saida} Km\n\n{HELP}\n"
    return saida
def f5(conn):
    conn.send("Entre com a idade:".encode(FORMAT))
    idade = int(read(conn))
    if(idade <= 7):
        saida = "Infantil A"
    else:
        if(idade <=10):
            saida = "Infantil B"
        else:
            if(idade <=13):
                saida = "juvenil A"
            else:
                if(idade <=17):
                    saida = "juvenil B"
                else:
                    saida = "Adulto"
    saida = f"\nSua categoria é {saida}\n\n{HELP}\n"
    return saida   
def f6(conn):
    conn.send("Entre com o nome:".encode(FORMAT))
    nome = read(conn)
    conn.send("Entre com o nivel:".encode(FORMAT))
    nivel = read(conn).upper()
    conn.send("Entre com o salario:".encode(FORMAT))
    salario = float(read(conn))
    conn.send("Entre com o número de dependentes:".encode(FORMAT))
    dependentes = int(read(conn))
    if(nivel =="A"):
        if(dependentes>0): 
            salario *= 0.92
        else:
            salario *= 0.97
    if(nivel =="B"):
        if(dependentes>0):
            salario *= 0.90
        else:
            salario *= 0.95
    if(nivel =="C"):
        if(dependentes>0):
            salario *= 0.85
        else:
            salario *= 0.92
    if(nivel =="D"):
        if(dependentes>0):
            salario *= 0.83
        else:
            salario *= 0.90
    saida = f"\n{nome} tem salario liquido de {salario}\n\n{HELP}\n"
    return saida
def f7(conn):
    conn.send("Entre com a idade:".encode(FORMAT))
    idade = int(read(conn))
    conn.send("Entre com a tempo de serviço:".encode(FORMAT))
    servico = int(read(conn))
    if(idade >= 65 or servico>=30 or (idade>=60 and servico>=25)):
        saida = "Já pode se aposentar"
    else: 
        saida = "Não pode se aposentar"
    saida = f"\n{saida}\n\n{HELP}\n"
    return saida
def f8(conn):
    conn.send("Entre com a Saldo Medio:".encode(FORMAT))
    saldo = float(read(conn))
    if(saldo <= 200):
        saida = "nenhum crédito"
    else:
        if(saldo <= 400):
            saida = "20'%' do valor do saldo médio"
        else:
            if(saldo <= 600):
                saida = "30'%' do valor do saldo médio"
            else:
                saida = "40'%' do valor do saldo médio"
    saida = f"\nSaldo medio de {saldo}, tem percentual de credito de {saida}\n\n{HELP}\n"
    return saida
def f9(conn):
    valor = random.randint(1,13)
    naipe = random.randint(1,4)
    if (valor == 11):
        valor = "Valete"
    if (valor == 12):
        valor = "Dama"
    if (valor == 13):
        valor = "Rei"
    if (valor == 1):
        valor = "Ás"
    if (naipe == 1):
        naipe = "Ouro"
    if (naipe == 2):
        naipe = "Paus"
    if (naipe == 3):
        naipe = "Copas"
    if (naipe == 4):
        naipe = "de Espadas"
    saida = f"\nSua carta é {valor} de {naipe}\n\n{HELP}\n"
    return saida

def read(conn):
    msg_length = conn.recv(HEADER).decode(FORMAT)
    msg_length = int(msg_length)
    msg = conn.recv(msg_length).decode(FORMAT)
    return msg

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    conn.send(HELP.encode(FORMAT))
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            print(f"msg = {msg}")
            if (msg == EXIT):
                connected = False
                conn.send("[DISCONNECTING...]".encode(FORMAT))
            else:
                if(int(msg)>0 and int(msg)<10):
                    if int(msg) == 1:
                        conn.send(f1(conn).encode(FORMAT))
                    if int(msg) == 2:
                        conn.send(f2(conn).encode(FORMAT))
                    if int(msg) == 3:
                        conn.send(f3(conn).encode(FORMAT))
                    if int(msg) == 4:
                        conn.send(f4(conn).encode(FORMAT))
                    if int(msg) == 5:
                        conn.send(f5(conn).encode(FORMAT))
                    if int(msg) == 6:
                        conn.send(f6(conn).encode(FORMAT))
                    if int(msg) == 7:
                        conn.send(f7(conn).encode(FORMAT))
                    if int(msg) == 8:
                        conn.send(f8(conn).encode(FORMAT))
                    if int(msg) == 9:
                        conn.send(f9(conn).encode(FORMAT))
                else: 
                    print(f"{msg} não e valido")
                    conn.send(f"[ERRO] {msg} não e valido".encode(FORMAT))
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


