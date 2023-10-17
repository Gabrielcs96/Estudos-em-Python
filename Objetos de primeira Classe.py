#Objetos de primeira Classe
#Em Py tudo é objeto, inclusive funçlões são objetos ! 
#Podemos atribuir funções a variáveis, passa-las como parâmetros para funções, usa-las como valores em estruturas de dados ( listas, tuplas, dicionários, etc.) e usar como valor de retorno para uma função ( clouseres)

def somar(a,b):
    return a+b

def multiplicar(a,b):
    return a*b

def subtrair(a,b):
    return a-b


def exibir_resultado(a,b,funcao):
    resultado = funcao(a,b)
    print(f"O resultado da operação é = {resultado}")

exibir_resultado(10,40,somar)
exibir_resultado(10,40,subtrair)
exibir_resultado(10,40,multiplicar)

op = somar

print(op(1,56))