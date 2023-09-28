#String e fatiamento - Hora de começarmos a trabalhar com strings em Python! 

curso = "pYtHon"

print(curso.upper()) #uppercase

print(curso.lower()) #lowercase

print(curso.title()) #passar para título 

print(curso.strip()) #remover espaços da variável/string

print(curso.lstrip()) #remover espaços da esquerda

print(curso.rstrip()) #remover espaços da direita

print(curso.center(20,'#')) # colocar coisas antes e depois da string - É útil para centralização!
print(curso.center(20)) # colocar coisas antes e depois da string - É útil para centralização!


print(".".join(curso)) #join de ponto em cada parte da string

print("-".join(curso.upper().center(20,"#")))


#Para interpolar variáveis é usado o método format e utilizando o f strings. 
# Hoje em dia , é mais utilizado o método f string


#OLD STYLE - PARECENDO C
nome = "Gabriel"
idade = 27
profissao = "cientista de dados"
linguagem = "SQL/Python"

print("Olá, me chamo %s. Eu tenho %d anos de idade e trabalho em %s eu domino as linguagens %s\n\n" %(nome, idade, profissao,linguagem))


#MÉTODO FORMAT - você consegue reaproveitar variáveis e colocar elas segundo a ordem que eu quiser  

print("Olá, me chamo {} Eu tenho {} anos de idade e trabalho como {} eu domino as linguagens {}" .format(nome, idade, profissao,linguagem))


print("Olá, me chamo {nome} Eu tenho {idade} anos de idade e trabalho como {profissao} eu domino as linguagens {linguagem}" .format(nome=nome, idade=idade, profissao=profissao,linguagem=linguagem))

pessoa ={ 
"nome" : "Gabriel",
"idade" : "27",
"profissao" : "cientista de dados",
"linguagem" : "SQL/Python"
}

print("Olá, me chamo {nome} Eu tenho {idade} anos de idade e trabalho como {profissao} eu domino as linguagens {linguagem}" .format(**pessoa))


#F-string ! 

nome = "Gabriel"
idade = 27
profissao = "cientista de dados"
linguagem = "SQL/Python"
saldo = 5749634.4345

print(f"TESTANDO O FSTRING \n Olá, me chamo {nome} Eu tenho {idade} anos de idade e trabalho como {profissao} eu domino as linguagens {linguagem} e o saldo desse mês é: {saldo:5.2f}" )



#Fatiamento de Strings  É uma técnica que é utilizada para retornar substrings ( partes da string original), informando início ( start), fim(stop) e passo(step): [sart: stop[,step]]

nomenovo = "Gabriel da Cruz Santos"

nomenovo[0]

nome[:10]

nome[5:]

print(nome[1,5:10])