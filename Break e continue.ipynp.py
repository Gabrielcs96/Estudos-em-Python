#Break e continue 

opcao = -1
while True:
    opcao = int(input("informe um número: "))

    if opcao == 10:
        print("\n k-bÔ!\n")
        break

    print(opcao)
    


for numero in range(100):
    if numero in (12,13,14,15):
        continue

    if numero == 99:
        break

    print(numero," ", end="")