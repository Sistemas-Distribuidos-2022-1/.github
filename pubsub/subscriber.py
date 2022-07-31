from ast import While
from curses.ascii import alt
import zmq
import random
import threading

PORT = "8000"
HOST = "127.0.0.1"
FORMAT = 'utf-8'


context = zmq.Context()
p = "tcp://"+ HOST +":"+ PORT

s1 = context.socket(zmq.SUB)
s1.connect(p)
s1.setsockopt_string(zmq.SUBSCRIBE, "f1")

s2 = context.socket(zmq.SUB)
s2.connect(p)
s2.setsockopt_string(zmq.SUBSCRIBE, "f2") 

s3 = context.socket(zmq.SUB)
s3.connect(p)
s3.setsockopt_string(zmq.SUBSCRIBE, "f3")

s4 = context.socket(zmq.SUB)
s4.connect(p)
s4.setsockopt_string(zmq.SUBSCRIBE, "f4")

s5 = context.socket(zmq.SUB)
s5.connect(p)
s5.setsockopt_string(zmq.SUBSCRIBE, "f5")

s6 = context.socket(zmq.SUB)
s6.connect(p)
s6.setsockopt_string(zmq.SUBSCRIBE, "f6")

s7 = context.socket(zmq.SUB)
s7.connect(p)
s7.setsockopt_string(zmq.SUBSCRIBE, "f7")

s8 = context.socket(zmq.SUB)
s8.connect(p)
s8.setsockopt_string(zmq.SUBSCRIBE, "f8")

s9 = context.socket(zmq.SUB)
s9.connect(p)
s9.setsockopt_string(zmq.SUBSCRIBE, "f9")

def f1(nome, cargo, salario):
    
    salario = float(salario)
    if cargo == "operador":
        salario *= 1.2
    else: 
        salario *= 1.18

    saida = f"\nReajuste de {nome} é R$ {salario}\n"
    #print(saida)
    return saida
def f2(nome, sexo, idade):

    idade=int(idade)
    if(idade >= 18 and sexo == "M"):
        saida = f"{nome} é Maior de idade"
    else: 
        if(idade >= 21 and sexo == "F"):
            saida = f"{nome} é Maior de idade"
        else:
            saida = f"{nome} é Menor de idade"
    saida = f"\n{saida}\n"
    return saida

def f3(N1,N2):
   
    N1=int(N1)
    N2=int(N2)
    if(((N2+N1)/2)>=7):
        saida = f"\nAprovado\n"
        return saida
    else:
        if(((N2+N1)/2)<=3):
            saida = f"\nReprovado\n"
            return saida
        else:
            print("Entre com o N3:".encode(FORMAT))
            N3 = int(input())
            if((((N2+N1)/2)+N3)/2 >=5):
                saida = f"\nAprovado\n"
                return saida
            else:
                saida = f"\nReprovado\n"
                return saida
def f4(sexo,altura):
    altura = float(altura)
    if(sexo == "M"):
        saida = (72.7 * altura) - 58
    else:
        saida =  (62.1 * altura) - 44.7
    saida = f"Peso ideal é {saida} Km\n"
    return saida
def f5(idade):
    idade = int(idade)
    
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
    saida = f"\nSua categoria é {saida}\n"
    return saida   
def f6(nome,nivel,salario,dependentes):
    salario = float(salario)
    dependentes = int(dependentes)
   
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
    saida = f"\n{nome} tem salario liquido de {salario}\n"
    return saida
def f7(idade,servico):

    idade = int(idade) 
    servico = int(servico)

    if(idade >= 65 or servico>=30 or (idade>=60 and servico>=25)):
        saida = "Já pode se aposentar"
    else: 
        saida = "Não pode se aposentar"
    saida = f"\n{saida}\n"
    return saida
def f8(saldo):
    saldo = float(saldo)
    
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
    saida = f"\nSaldo medio de {saldo}, tem percentual de credito de {saida}\n"
    return saida
def f9(entrada):
    entrada=entrada
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
    saida = f"\nSua carta é {valor} de {naipe}\n"
    return saida

def read1(s1):
    entrada = s1.recv().decode(FORMAT).split("@")
    print(entrada)
    saida = f1(entrada[1],entrada[2],entrada[3])
    print(saida)

def read2(s2):
    entrada = s2.recv().decode(FORMAT).split("@")
    print(entrada)
    saida = f2(entrada[1],entrada[2],entrada[3])
    print(saida)

def read3(s3):
    entrada = s3.recv().decode(FORMAT).split("@")
    print(entrada)
    saida = f3(entrada[1],entrada[2])
    print(saida)

def read4(s4):
    entrada = s4.recv().decode(FORMAT).split("@")
    print(entrada)
    saida = f4(entrada[1],entrada[2])
    print(saida)

def read5(s5):
    entrada = s5.recv().decode(FORMAT).split("@")
    print(entrada)
    saida = f5(entrada[1])
    print(saida)

def read6(s6):
    entrada = s6.recv().decode(FORMAT).split("@")
    print(entrada)
    saida = f6(entrada[1],entrada[2],entrada[3],entrada[4])
    print(saida)

def read7(s7):
    entrada = s7.recv().decode(FORMAT).split("@")
    print(entrada)
    saida = f7(entrada[1],entrada[2])
    print(saida)

def read8(s8):
    entrada = s8.recv().decode(FORMAT).split("@")
    print(entrada)
    saida = f8(entrada[1])
    print(saida)

def read9(s9):
    entrada = s9.recv().decode(FORMAT)
    print(entrada)
    saida = f9(entrada)
    print(saida)


while True:
    t1 = threading.Thread(target=read1, args=[s1])
    t2 = threading.Thread(target=read2, args=[s2])
    t3 = threading.Thread(target=read3, args=[s3])
    t4 = threading.Thread(target=read4, args=[s4])
    t5 = threading.Thread(target=read5, args=[s5])
    t6 = threading.Thread(target=read6, args=[s6])
    t7 = threading.Thread(target=read7, args=[s7])
    t8 = threading.Thread(target=read8, args=[s8])
    t9 = threading.Thread(target=read9, args=[s9])
    try:
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        t7.start()
        t8.start()
        t9.start()
    except:
        pass
