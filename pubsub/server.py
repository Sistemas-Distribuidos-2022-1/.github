from ast import While
from multiprocessing import connection
from venv import create
from database import IO, Client, Connections
from datetime import datetime
import zmq
import string
import threading
import random
import peewee
import time

FORMAT = 'utf-8'
HEADER = 64
PORT = "8080"
HOST = "127.0.0.1"
ADDR = (HOST, PORT)
EXIT = "exit"
HELP = "[HELP] Entre com o némero função entre 1 e 9 ou \"exit\" para sair:"


print(f"[SERVER]:\tADDR = {ADDR}")

def f1(s):
    s.send_string("Entre com o nome:".encode(FORMAT))
    nome = read(conn)
    s.send_string("Entre com o cargo:".encode(FORMAT))
    cargo = read(conn).lower()
    s.send_string("Entre com o salario:".encode(FORMAT))
    salario = float(read(conn))

    if cargo == "operador":
        salario *= 1.2
    else: 
        salario *= 1.18

    saida = f"\nReajuste de {nome} é R$ {salario}\n\n{HELP}"
    #print(saida)
    return saida
def f2(s):
    s.send_string("Entre com o nome:".encode(FORMAT))
    nome = read(conn)
    s.send_string("Entre com o sexo (M ou F):".encode(FORMAT))
    sexo = read(conn).upper()
    s.send_string("Entre com a idade:".encode(FORMAT))
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
def f3(s):
    s.send_string("Entre com o N1:".encode(FORMAT))
    N1 = int(read(conn))
    s.send_string("Entre com o N2:".encode(FORMAT))
    N2 = int(read(conn))
    if(((N2+N1)/2)>=7):
        saida = f"\nAprovado\n\n{HELP}\n"
        return saida
    else:
        if(((N2+N1)/2)<=3):
            saida = f"\nReprovado\n\n{HELP}\n"
            return saida
        else:
            s.send_string("Entre com o N3:".encode(FORMAT))
            N3 = int(read(conn))
            if((((N2+N1)/2)+N3)/2 >=5):
                saida = f"\nAprovado\n\n{HELP}\n"
                return saida
            else:
                saida = f"\nReprovado\n\n{HELP}\n"
                return saida
def f4(s):
    s.send_string("Entre com o sexo (M ou F):".encode(FORMAT))
    sexo = read(conn).upper()
    s.send_string("Entre com a altura:".encode(FORMAT))
    altura = float(read(conn))
    if(sexo == "M"):
        saida = (72.7 * altura) - 58
    else:
        saida =  (62.1 * altura) - 44.7
    saida = f"Peso ideal é {saida} Km\n\n{HELP}\n"
    return saida
def f5(s):
    s.send_string("Entre com a idade:".encode(FORMAT))
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
def f6(s):
    s.send_string("Entre com o nome:".encode(FORMAT))
    nome = read(conn)
    s.send_string("Entre com o nivel:".encode(FORMAT))
    nivel = read(conn).upper()
    s.send_string("Entre com o salario:".encode(FORMAT))
    salario = float(read(conn))
    s.send_string("Entre com o número de dependentes:".encode(FORMAT))
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
def f7(s):
    s.send_string("Entre com a idade:".encode(FORMAT))
    idade = int(read(conn))
    s.send_string("Entre com a tempo de serviço:".encode(FORMAT))
    servico = int(read(conn))
    if(idade >= 65 or servico>=30 or (idade>=60 and servico>=25)):
        saida = "Já pode se aposentar"
    else: 
        saida = "Não pode se aposentar"
    saida = f"\n{saida}\n\n{HELP}\n"
    return saida
def f8(s):
    s.send_string("Entre com a Saldo Medio:".encode(FORMAT))
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
def f9(s):
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

def read(s):
    msg = s.recv()
    return msg

def handle_client(s,p, context, connectionTime):

    print(f"[SERVER]:\t[NEW CONNECTION] s= {s}, p= {p}, context= {context} connected.")
    
    if(True):
        #DB save cliente ADDR

        addr = p

        try:
            cliente_cliente = Client.create(
                addrClient = addr
            )
            print(f"[DATABASE]:\t{addr} Foi cadastrado.")
        except:
            cliente_cliente = Client.select().where(Client.addrClient == addr)
            print(f"[DATABASE]:\t{addr} Já esta cadastrado.")

        #DB save cliente connection time
        try:
            client_connetions = Connections.create(
                fromClient = cliente_cliente,
                timeConnection = connectionTime 
            )
            print(f"[DATABASE]:\tconexão [SALVO] no banco de dados.")
        except:
            print(f"[DATABASE]:\t[ERRO] não foi possivel salvar as conexões banco de dados.")

        #receiver and processing msg from CLIENT
        while True:
            s.send_string("OI" + HELP)

        connected = False
        while connected:
            

            msg = s.recv().decode(FORMAT)
            recivedTime = datetime.now()

            if (msg == EXIT):
                connected = False
                msgToClinte = f"[SERVER]:\t{addr} [DESCONNECTING] ...\n"
                s.send_string(msgToClinte.encode(FORMAT))
                sededTime = datetime.now()

                #DB
                try:
                    client_connetions.timeDisconnection = datetime.now()
                    client_connetions.save()
                    print(f"[DATABASE]:\tDesconexão [SALVO] no banco de dados.")
                except:
                    print(f"[DATABASE]:\t[ERRO] não foi possivel salvar as desconexões banco de dados.")
                    

            else:
                if(int(msg)>0 and int(msg)<10):
                    if int(msg) == 1:
                        msgToClinte = f1(s)
                        s.send_string(msgToClinte.encode(FORMAT))
                    if int(msg) == 2:
                        msgToClinte = f2(s)
                        s.send_string(msgToClinte.encode(FORMAT))
                    if int(msg) == 3:
                        msgToClinte = f3(s)
                        s.send_string(msgToClinte.encode(FORMAT))
                    if int(msg) == 4:
                        msgToClinte = f4(s)
                        s.send_string(msgToClinte.encode(FORMAT))
                    if int(msg) == 5:
                        msgToClinte = f5(s)
                        s.send_string(msgToClinte.encode(FORMAT))
                    if int(msg) == 6:
                        msgToClinte = f6(s)
                        s.send_string(msgToClinte.encode(FORMAT))
                    if int(msg) == 7:
                        msgToClinte = f7(s)
                        s.send_string(msgToClinte.encode(FORMAT))
                    if int(msg) == 8:
                        msgToClinte = f8(s)
                        s.send_string(msgToClinte.encode(FORMAT))
                    if int(msg) == 9:
                        msgToClinte = f9(s)
                        s.send_string(msgToClinte.encode(FORMAT))
                    sededTime = datetime.now()
                else:
                    print(f"[SERVER]:\t{msg} não e valido")
                    msgToClinte = f"[SERVER]:\t[ERRO] {msg} não e valido"
                    s.send_string(msgToClinte.encode(FORMAT))
                    sededTime = datetime.now()
            
            #DB save msg receiver and sended 
            try:
                cliente_io = IO.create(
                    fromClient = cliente_cliente, 
                    messageReciver = msg,
                    messageSender = msgToClinte,
                    timeReciver = recivedTime,
                    timeSender = sededTime
                )
                print(f"[DATABASE]:\tInput e output [SALVO] no banco de dados.")
            except:
                print(f"[DATABASE]:\t[ERRO] não foi possivel salvar input e output no banco de dados.")

    #conn.close()

def start():
    context = zmq.Context()
    s = context.socket(zmq.PUB)             # create a publisher socket
    p = "tcp://"+ HOST +":"+ PORT           # how and where to communicate
    s.bind(p)                               # bind socket to the address
    connectionTime = datetime.now()
    
    while True:
            s.send_string("OI" + HELP)


    #handle_client(s,p, context, connectionTime)



    #mult thread
    if(False):
        print(f"[SERVER]:\t[LISTENING] Server is listening on {ADDR}")
        while True:
            connectionTime = datetime.now()
            thread = threading.Thread(target=handle_client, args=(s,p, context, connectionTime))
            thread.start()
            print(f"[SERVER]:\t[CONEXÕES ATIVAS] = {threading.activeCount() - 1}")

print("[SERVER]:\tIniciando ...")
start()



