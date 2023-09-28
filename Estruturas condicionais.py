# estruturas condicionais são estruturas que permitem o desvio de fluxo de controle 

def habilitacao(idade):
    if idade >= 18:
        print("você pode tirar a habilitação")
    


habilitacao(24)


def habilitacao(idade):
    if idade >= 18:
        print("você pode tirar a habilitação")
    else:
        print("Você não pode tirar a habilitação porque é menor de idade")    

habilitacao(17)


#def saque(saque):
saldo = 2000.0
saque = input("informe o valor do saque:")

if saldo>= saque: 
    print("Realizando saque...")
    print("retire o seu dinheiro na boca do caixa")

if saldo< saque:
    print(" V+ocê não pode sacar. Saldo insuficiente")





saldo = 2000.0
saque = float(input("informe o valor do saque: "))

if saldo > saque:
    print("Seu saldo é maior que o saque")
else:
    print("Seu saldo é menor que o saque")




#Elif

opcao = int(input("Informe uma opção [1] - Sacar \n [2] - Extrato "))

if opcao ==1:
    valor= float(input("Informe a quantia para o saque: "))
elif opcao == 2:
    print("Exbindo extrato... ")
else:
    sys.exit("Opção inválida")

