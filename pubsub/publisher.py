import zmq

PORT = "8000"
HOST = "127.0.0.1"
HELP = "[HELP] Entre com o némero função entre 1 e 9 ou \"exit\" para sair:"

context = zmq.Context()
s = context.socket(zmq.PUB)
p = "tcp://"+ HOST +":"+ PORT
s.bind(p)

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

                saida = f"@{nome}@{cargo}@{salario}"
                s.send_string("f1" + saida)
        if(run == 2):
                print("Entre com o nome:")
                nome = input()
                print("Entre com o sexo (M ou F):")
                sexo = input().upper()
                print("Entre com a idade:")
                idade = int(input())

                saida = f"@{nome}@{sexo}@{idade}"
                s.send_string("f2" + saida)
        if(run == 3):
                print("Entre com o N1:")
                N1 = int(input())
                print("Entre com o N2:")
                N2 = int(input())

                saida = f"@{N1}@{N2}"
                s.send_string("f3" + saida)
        if(run == 4):
                print("Entre com o sexo (M ou F):")
                sexo = input().upper()
                print("Entre com a altura:")
                altura = float(input())

                saida = f"@{sexo}@{altura}"
                s.send_string("f4" + saida)
        if(run == 5):
                print("Entre com a idade:")
                idade = int(input())
                saida = f"@{idade}"
                s.send_string("f5" + saida)

        if(run == 6):
                print("Entre com o nome:")
                nome = input()
                print("Entre com o nivel:")
                nivel = input().upper()
                print("Entre com o salario:")
                salario = float(input())
                print("Entre com o número de dependentes:")
                dependentes = int(input())

                saida = f"@{nome}@{nivel}@{saida}@{dependentes}"
                s.send_string("f6" + saida)

        if(run == 7):
                print("Entre com a idade:")
                idade = int(input())
                print("Entre com a tempo de serviço:")
                servico = int(input())

                saida = f"@{idade}@{servico}"
                s.send_string("f7" + saida)

        if(run == 8):
                print("Entre com a Saldo Medio:")
                saldo = float(input())
                saida = f"@{saldo}"
                s.send_string("f8" + saida)

        if(run == 9):
                s.send_string("f9" + "@")


        print(HELP)
        run = input()
        