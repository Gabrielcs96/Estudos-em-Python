
pessoa ={ "Gabs": {"nome": "Gabriel","idade":27}
}

pessoa2 = dict(nome="Fulano", idade=10)

pessoa["telefone"]= 71993262683

#Método clear - limpar dicionário 

pessoa2.clear()
print(pessoa)
print(pessoa2)

#Método copy - cria uma cópia do nosso dicionário 

copia = pessoa.copy()

copia["Gabs"]={"nome":"Gabs teste"}
print(copia)

#keys é uma função que você usa para descobrir quais "keys" você tem no seu dicionário

novo_dicionario = {"a":100, "b":"teste", 3:"Python"}

print(novo_dicionario.keys())

#pop  - Remover uma chave do seu dicionário. VoCê pode por a sua chave e se ela não existir, você pode fazer ela retornar um valor padrão. 

contato = {"gabs.sts": {"nome": "Gabriel", "@":"@Gabscs96"}}

resultado = contato.pop("gabs.sts","apagado")

print(resultado)


#popitem - remoção dos itens na sequência 

contato = {"gabs.sts": {"nome": "Gabriel", "@":"@Gabscs96"}}
contato.popitem()


#Setdefault 

contato_a = {"nome": "Gabriel", "@":"@Gabscs96"}

contato_a.setdefault("Idade",27)

print(contato_a)


#update - Atualizar, você consegue fazer modificações dentro do dicionário, onde, por exemplo, você já tem uma chave. 

contato_a.update({"nome":"Gabs"})

print(contato_a)

#values - Vai retornar para nós todos valores, ao invés das chaves, como o " keys". 

print(contato_a.values())

#in - É uma forma elegante de saber se existe um determinado conteúdo dentro do cionário 
#Usamos da seguinte forma: 

resultado_a = "nome" in contato_a
print(resultado_a)

resultado_a = "Gabs" in contato_a

#Del - Você passa qual o objeto que você quer remover e ele remove. 



contato_a = {"teste":{"nome": "Gabriel", "@":"@Gabscs96"},
             "teste2":{"nome": "Gabs", "@":"@Gabscs96ssss"}}

del contato_a["teste"]
print(contato_a)

del contato_a["teste2"]["@"]
print(contato_a)