#Escopo local e global 
# dentro do bloco da função é de escopo local. Quando a função é finalizada, tudo o que está lá morre. 
# Agora, se você está usando objetos que são mutáveis ( que vem de fora da função, você poderá ver que a função mudará)
#No entanto, se você quer que a função faça mudanças globais, você deverá usar  a palavra reservada 'Global', que informa ao interpretador que a variável está sendo manipulada no escopo global - Essa é uma prática que deve ser evitada

salario = 50000


def salario_bonus(bonus):
    global salario 
    salario += bonus
    return salario

print(salario_bonus(3500))

lista = [1]
lista_aux=lista.copy()
lista_aux.append(3)
print(lista)
print(lista_aux)