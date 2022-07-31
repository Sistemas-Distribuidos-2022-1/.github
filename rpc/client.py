import xmlrpc.client

PORT = 8080
HOST = "127.0.0.1"
IP = f"http://{HOST}:{PORT}"
HELP = "[HELP] Entre com o némero função entre 1 e 9 ou \"exit\" para sair:"
FORMAT = 'utf-8'

proxy = xmlrpc.client.ServerProxy(IP)

print(HELP)
run = input()
while(run != "exit"):
    run=int(run)
    if(run == 1):
        print("Entre com o nome:")
        nome = input()
        print("Entre com o cargo:")
        cargo = input().lower()
        print("Entre com o salario:")
        salario = float(input())

        print("%s" % str(proxy.f1(nome, cargo, salario)))
    if(run == 2):
        print("Entre com o nome:")
        nome = input()
        print("Entre com o sexo (M ou F):")
        sexo = input().upper()
        print("Entre com a idade:")
        idade = int(input())

        print("%s" % str(proxy.f2(nome, sexo, idade)))
    if(run == 3):
        print("Entre com o N1:")
        N1 = int(input())
        print("Entre com o N2:")
        N2 = int(input())

        print("%s" % str(proxy.f3(N1,N2)))
    if(run == 4):
        print("Entre com o sexo (M ou F):")
        sexo = input().upper()
        print("Entre com a altura:")
        altura = float(input())

        print("%s" % str(proxy.f4(sexo,altura)))
    if(run == 5):
        print("Entre com a idade:")
        idade = int(input())

        print("%s" % str(proxy.f5(idade)))
    if(run == 6):
        print("Entre com o nome:")
        nome = input()
        print("Entre com o nivel:")
        nivel = input().upper()
        print("Entre com o salario:")
        salario = float(input())
        print("Entre com o número de dependentes:")
        dependentes = int(input())

        print("%s" % str(proxy.f6(nome,nivel,salario,dependentes)))
    if(run == 7):
        print("Entre com a idade:")
        idade = int(input())
        print("Entre com a tempo de serviço:")
        servico = int(input())

        print("%s" % str(proxy.f7(idade,servico)))
    if(run == 8):
        print("Entre com a Saldo Medio:")
        saldo = float(input())

        print("%s" % str(proxy.f8(saldo)))
    if(run == 9):
        print("%s" % str(proxy.f9()))
    
    run = input()