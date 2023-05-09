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
    caractere ()
    print ( "Realizado com susseço" )
    caractere ()
    print("-"* 15)
    for n in range (1,11):
        print ( f"| { num } x { n } = { num * n } " )
    print("-"* 15)
    sair = str(input("Deseja continuar?[S/N]")).lower()
   
    if sair == 'n':
    	break
    elif sair == 's':
    	continuar
imprimir ( "pix: jonatascleber123@gmail.com" )
imprimir ( "volte sempre!")
