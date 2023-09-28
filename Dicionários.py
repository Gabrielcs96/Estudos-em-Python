# Os dicionários são um conjunto não ordenado de par, chave valor. Diferentemente das listas, tuplas e conjuntos. Há sempre pares chave-valor
#podemos usar o construtor dict e/ou podemos usar a criação usual de {"":""}
# se assmelha muito a estruta  " usual " de criação de objetos em JS 

pessoa ={"nome": "Gabriel","idade":27}

pessoa2 = dict(nome="Fulano", idade=10)

pessoa["telefone"]= 71993262683

print(pessoa["idade"])

#dicionários aninhados - Naturalmente dicionários podem armezenar qualquer tipo de objeto python como valor, desde que a chave para esse valor seja imutável ( como strings e números).
#logo, você pode colocar dicionários dentro do dicionário

contatos = {
    "gabriel.sts":{"nome":"Gabriel","telefone":"71993262683"},
    "Maria.sts":{"nome":"Maria","telefone":"123456789"},
    "Bdo.sts":{"nome":"Bdo","telefone":"987654321"}
}

telefone= contatos["gabriel.sts"]["telefone"]
print(telefone)

extra = contatos["Bdo.sts"]

print(extra)
print("\n")

#iterar sobre dicionários 

for chave in contatos:
    print(chave,contatos[chave])

print("\n")

for chave, valor in contatos.items():
   print(chave, valor)
   
pessoa2["nome"]="fulano2"

print(pessoa2)