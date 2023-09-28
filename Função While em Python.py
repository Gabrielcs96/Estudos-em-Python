#While agora 

opcao = -1

while opcao !=0:
    opcao = int(input("\n[1] - Sacar \n [2] Extrato: "))
    
    if opcao == 1:
        print("Sacando... \n")
    elif opcao == 2:
        print("Exibindo o seu extrato... \n")

    else:
        print("Obrigado por usar o nosso sistema bancário, até mais!")