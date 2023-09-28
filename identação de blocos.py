

def sacar (valor):
    saldo=500
    
    if saldo>= valor:
        print("Valor sacado!")
        print("Retire o seu dinheiro na boca do caixa")
    else:
        print("Você não tem saldo suficiente para concluir essa operação")

    print("Obrigado por ser nosso cliente, tenha um bom dia")

def depositar(valor):
    saldo=500
    saldo+=valor
    print(saldo)

depositar(200)
sacar(300)


