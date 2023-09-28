#Operadores de identidade 
# São operadores utilizados para comparar se os dois objetos testados ocupam a mesma posição na memória. 
# O operador " is " é o responsável por fazer essa comparação para saber se ambos utilizam a mesma região de memória.

curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

curso is nome_curso
# >>> True

curso is not nome_curso 
# >>> False 

saldo is limite 
# >>> True 


saldo1= 1000
limite = 500

print(saldo1 is limite)

print(saldo1 is not limite)