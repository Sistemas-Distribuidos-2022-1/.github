import random
from xmlrpc.server import SimpleXMLRPCServer

PORT = 8080
HOST = "127.0.0.1"
FORMAT = 'utf-8'
HELP = "[HELP] Entre com o número função entre 1 e 9 ou \"exit\" para sair:"


def f1(nome, cargo, salario):
    

    if cargo == "operador":
        salario *= 1.2
    else: 
        salario *= 1.18

    saida = f"\nReajuste de {nome} é R$ {salario}\n\n{HELP}"
    #print(saida)
    return saida
def f2(nome, sexo, idade):

    if(idade >= 18 and sexo == "M"):
        saida = f"{nome} é Maior de idade"
    else: 
        if(idade >= 21 and sexo == "F"):
            saida = f"{nome} é Maior de idade"
        else:
            saida = f"{nome} é Menor de idade"
    saida = f"\n{saida}\n{HELP}\n"
    return saida

def f3(N1,N2):
   
    if(((N2+N1)/2)>=7):
        saida = f"\nAprovado\n\n{HELP}\n"
        return saida
    else:
        if(((N2+N1)/2)<=3):
            saida = f"\nReprovado\n\n{HELP}\n"
            return saida
        else:
            print("Entre com o N3:".encode(FORMAT))
            N3 = int(input())
            if((((N2+N1)/2)+N3)/2 >=5):
                saida = f"\nAprovado\n\n{HELP}\n"
                return saida
            else:
                saida = f"\nReprovado\n\n{HELP}\n"
                return saida
def f4(sexo,altura):
    
    if(sexo == "M"):
        saida = (72.7 * altura) - 58
    else:
        saida =  (62.1 * altura) - 44.7
    saida = f"Peso ideal é {saida} Km\n\n{HELP}\n"
    return saida
def f5(idade):
    
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
def f6(nome,nivel,salario,dependentes):
   
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
def f7(idade,servico):

    if(idade >= 65 or servico>=30 or (idade>=60 and servico>=25)):
        saida = "Já pode se aposentar"
    else: 
        saida = "Não pode se aposentar"
    saida = f"\n{saida}\n\n{HELP}\n"
    return saida
def f8(saldo):
    
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
def f9():
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

server = SimpleXMLRPCServer((HOST, PORT), logRequests=True)
server.register_function(f1, "f1")
server.register_function(f2, "f2")
server.register_function(f3, "f3")
server.register_function(f4, "f4")
server.register_function(f5, "f5")
server.register_function(f6, "f6")
server.register_function(f7, "f7")
server.register_function(f8, "f8")
server.register_function(f9, "f9")

try:
    print(f"[SERVER]:\t[LISTENING] Server is listening on {HOST}:{PORT}")

    server.serve_forever()

except:
    print("[SERVER]:\tDisecting...")

