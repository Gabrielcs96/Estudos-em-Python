#Estruturas de repetição - Vamos trabalhar com While e For. 

a = int(input("informe um número inteiro: "))
print(a)
a+=1
print(a)

a+=1
print(a)




# usando for agora !
text = input("Informe um texto: ")
VOGAIS ='AEIOU'

for letra in text:
    if letra.upper() in VOGAIS: # o upper só serve para por as letras de minúsculo, para maiúculo 
        print(letra, end="")
else:
    print("\n")
    print("Fim do texto ")
#for else - ERsse só existe como um if/else mesmo, só é uma alternativa para a execução quando o for acabar ! 


# Função range - Usada para gerar números inteiros em python


a = int(input("Digite um número "))
qtd = int(input("informe até onde você quer que o número seja iterado:  "))
if a<qtd:
    for a in range(a,qtd):
        print(a,end="")
else:
  print("impossível realizar a operação desejada! ")


print("imprimindo todos os carinhas das condilões a baixo ")
for numero in range(0,51,5):
    print(numero, end="")


#While agora 

opcao = -1

while opcao !=0:
    opcao = int(input("[1] - Sacar \n [2] Extrato"))
    
    if opcao == 1:
        print("Sacando... ")
    elif opcao == 2:
        print("Exibindo o seu extrato... ")