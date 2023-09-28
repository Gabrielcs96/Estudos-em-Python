#Operadores de associação

#São operadore sutilizados para verificar se um objeto está presente numa sequência 
# o operador aqui é o " in ", para saber se está contido. 
# lembrar que é case sensitive 



curso = "Curso de Python"
frutas = ["laranja", "uva", "limão"]
saques = [1500, 100]

"Python" in curso 
# >>> True 

"Maçã"  not in frutas
# >>> True

200 in saques 
# >>> False

print("limão" not in frutas)
# >>> False
