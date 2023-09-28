#Conjunto de sets - um set é uma coleção que não possui objetos repetidos, usamos sets para representar conjuntos matemáticos. Ele "exclui" valores repetidos 
#O Set não garante ordens ! É sempre importante você ordenar posteriormente 

print(set(['1','2','3','1','4','5','2 ']))


print(set("abacaxi"))

print(set(("palio","gol","celta","palio")))

#conjuntos de python não aceitam indexação nem fatiamento, caso você queira consumir os valores, é necessário usar uma lista 

numeros = {1,2,3,1,2,3,1,2,3}

numeros = list(numeros)

print(numeros[1])

#iterar dentro de um for 
carros = {"palio","gol","celta"}

for carro in carros:
    print(carro)

    
#função enumerate - as vezes é necessário saber qual o índice do objeto dentro do laço for. Para isso podemos usar a função enumerate

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")




#MÉTODOS DE CLASSE SET


#Union 
  
conjunto_a= {1,1,2}
conjunto_b= {3,4,1,2,2,2,2,2}

conj_ab=conjunto_a.union(conjunto_b)
print(conj_ab)

#intersection - saber o que tem em um que tem no outro 

conj_c=conjunto_a.intersection(conjunto_b)
print(conj_c)

#diference -  o que é diferente de um conjunto para outro 

conj_d= conjunto_a.difference(conjunto_b)
conj_e= conjunto_b.difference(conjunto_a)

print(conj_d)
print(conj_e)

#simetric difference - qual a diferença que 

conj_diff=conjunto_a.symmetric_difference(conjunto_b)

print(conj_diff)

#issubset - saber se algum deles é tem números dentro deles que é o mesmo que se tem no outro conjunto, ou seja, saber se é um subconjunto 


conj_1={1,2,3}
conj_2={4,1,2,5,6,3}

print(conj_1.issuperset(conj_2))

print(conj_2.issuperset(conj_1))


#isdisjoint - todos os elementos de um conjunto não estão presentes em outro conjuntos, ou seja são conjuntos que não se tocam 

conja = {1,2,3,4,5}
conjb = {6,7,8,9}
conjc = {1,0}

print(conja.isdisjoint(conjb))
print(conja.isdisjoint(conjc))

#.add - que serve para passar elementos e adicionar esses elementos ao conjunto, exemplo: 

sorteio = {1,26}

sorteio.add(25)
sorteio.add(23)
sorteio.add(20)

#clear - Limpar o conjunto 

sorteio2 = {1,26}

sorteio2.clear()

# Discard que é nada mais nada menos que descartar números específicos de dentro do conjunto 


conja = {1,2,3,4,5}

conja.discard(4)
print(conja)

#pop - Tirar valores como numa pilha 

# o remove, se o número não existir, ele d´aum erro, diferentemente do discard 