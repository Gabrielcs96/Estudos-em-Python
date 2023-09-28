conta_normal: True
Conta_universitaria: False

saldo = 2000
saque= 2500
cheque_especial= 450


if conta_normal:
    if saldo>= saque: 
        print("Saque Realizado com sucesso")
    elif saque <= (saldo+ cheque_especial):
        print("Saque realizad com uso do cheque especial!")
    else:
        print("Não foi possível executar o saque! Saldo insuficiente")
    
elif Conta_universitaria:
    if saldo>= saque:
        print("Saque realizado com sucesso")
    else: print("Saldo insuficiente")

else:
    print("O sistema não reconheceu o seu tipo de conta! Entre em contato com o seu gerente")

