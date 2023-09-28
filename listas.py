#Listas ! Listas são elementos mutáveis que podem armazenar qualquer tipo de objeto. Podemos criar listas a partir do construtor " list " ou usando valores separados por vírgulas, dentro de colchetes. 

frutas = ["Laranja", "maca", "uva"]
print(frutas)
frutas2 = []
print(frutas2)
letras = list("python")
print(letras)
numeros = list(range(10))
print(numeros)
carro= ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
print(carro)

#listas devem ser acessadas de forma sequencial ! 

frutas = ["Laranja", "maca", "uva", "pêra"]
frutas[1]
frutas[0]
frutas[-1]
frutas[-3]

#listas aninhadas podem representar matrizes ! 

Exemplo = [
    [1,2,"a"],
    ["b",3,4],
    ["k", "c", 6]
]

Exemplo[0]
Exemplo[0][1]
Exemplo[0][-1]
Exemplo[-1][-2]


#Fatiamento - Acessar conjuntos de elementos a partir do início, fim e passos do que eu quiser ! 

lista = list("python")
lista[2:]
lista[:2]
lista[1:3]
lista[0:3:2]
lista[::-1]

carro1 = ["gol","celta","palio"]

for carros in carro1:
    print(carros)

#função Enumerate

for indice, carro in enumerate(carro1):
    print(f'{indice}: {carro1[indice]}')



#Compreensão de listas

# serve para você criar uma nova lista a partir de uma lista existente, de forma performática 
numeros = [0,1,30,21,2,9,65,374,16,4,3,7]
pares=[]

for numero in numeros:
    if numero%2 == 0:
        pares.append(numero)

print(pares)

#Agora com o compreehension

numeros2 = [0,1,30,21,2,9,65,374,16,4,3,7]
pares = [numero for numero in numeros2 if numero%2==0]
print(pares)