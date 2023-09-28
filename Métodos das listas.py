#Métodos das listas
#append 


lista =[]

lista.append(1)
lista.append("python")
lista.append([35,37,44,12])

print(lista)

#clear

list = lista

print(list)

list.clear()
print(list)

l2 = lista.copy()
print(l2)

#extends-- Para juntar duas listas ou mais 

#count - Utilizado para contar a quantidade de vezes que um determinado objeto aparece dentro de uma determinada lista ! 
#exemplo

listacores=['verde','amarelo','vermelho','verde','amarelo']

listacores.count('verde')

listacores.extend(['js','carvalho'])

print(listacores)

#index - Demonstrar qual que é a primeira ocorrência de um determinado objeto 

linguagens = ['js','c','c++','python','js']

print(linguagens.index('c++'))


#pop - Remover um dado de dentro da lista, como numa pilha. Você pode também selecionar a posição do dado !

testando_lingagens=['p','a','s','d']

testando_lingagens.pop(0)

print(testando_lingagens)

#remove - remoção por semelhança 
testando_lingagens=['p','a','s','d']
testando_lingagens.remove('a')

print(testando_lingagens)


#reverese - Reverte a ordem das coisas 
linguagens = ['js','c','c++','python','js']

linguagens.reverse()

print(linguagens)


#sort -- Ordenação, você passa uma chave/argumento para fazer com que ele faça a ordenação a partir de desses termos

linguagens.sort()
print(linguagens)

linguagens.sort(key=lambda x: len(x)) #ordenar por tamanho das palavras

#len - Dizer a quantidade de elementos que tem naquela lista 

print(len(linguagens))
#sorted 