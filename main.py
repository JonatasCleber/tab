import os

while True:
    def caractere():
    	print("-"*23)
    os.system("clear")
    caractere()
    print("me apoie no pix")
    print("pix: jonatascleber123@gmail.com")
    caractere()
    num = int(input("Digite o numero da tabuada: "))
    print("")
    print("-"* 23)
    print("Realizado com susseço")
    print("-"*23)
    print("-"* 15)
    for n in range (1,11):
        print(f"|{num} x {n} = {num*n}")
    print("-"* 15)
    sair = str(input("Deseja continuar?[S/N]")).lower()
   
    if sair == 'n':
    	break
    elif sair == 's':
    	continue