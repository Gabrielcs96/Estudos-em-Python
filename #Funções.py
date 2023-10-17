#Funções
# Funções são blocos de códigos que poderão ser reutilizados ao longo do código! 
#É uma função como em qualquer outra linguagem! 

#Programar usando funções é o mesmo que programar de forma estruturada ( em relação ao paradigma)

def exibir_mensagem():
    print("Olá Mundo!")

def exibir_mensagem_2(nome):
        print(f"Seja bem vindo {nome}")

def exibir_mensagem_3(nome="anônimo"):
      print(f"Seja bem vindo(a) {nome}!") 


exibir_mensagem()
exibir_mensagem_2(nome= "Gabriel")
exibir_mensagem_3()
exibir_mensagem_3(nome="Sara")

exibir_mensagem_2("Astolfo")

#Como em Python você pode retornar diversos valores na mesma função:

def calcular_total(numeros):
      return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
      antecessor = numero - 1
      sucessor = numero + 1 

      return sucessor, antecessor

def funcao():
      print("Aqui não precisa de retorno explicito")
      return None

print(calcular_total([4,5]))

print(retorna_antecessor_e_sucessor(65))

funcao()

#Argumento nomeado é o argumento que você iforma chave/valor

def salvar_carro(marca, modelo, ano, placa):
      print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Fiat","Palio",2007,"ABC9N744")

# a desvantagem de passar dessa forma é que se o usuário informar 

salvar_carro(marca="Kia",modelo="Sportage",ano=2017,placa="ABC-1234")

salvar_carro(**{"marca":"BMW","modelo":"X3","ano":2021,"placa":"BCA-4321"})


#Args e Kwargs - Podemos combinar parâmetros obrigatórios com args e kwargs. Quando esses são definidos (*args e **kwargs), o método recebe os valores como tupla e dicionario respectivamente
#Exemplo 

def exibir_poemas(data_extenso, *args, **kwargs):
      texto= "\n".join(args)
      meta_dados ="\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
      mensagem = f"{data_extenso}\n\n{texto} \n\n {meta_dados}"
      
      print(mensagem)
      return None

exibir_poemas("Zen of Python", "Beautiful is better than Ugly.", autor = "Tim Petters", ano=1999)


#args e kwargs - extendido 

def calcular_imposto(valor, perc_ir):
      ir = valor * 0.275
      iss = valor * 0.05
      csll = valor * 0.0375
      pis = valor * 0.03
      return ir + iss+ csll + pis

print(calcular_imposto(1000, 0.275))

print(calcular_imposto(perc_ir=0.275, valor=2000 ))

#ARGUMENTOS DE POSIÇÃO TEM QUE, OBRIGATORIAMENTE SER OS PRIMEIROS A SEREM PASSADOS SENÃO DÁ ERRO 
print(calcular_imposto(2000, perc_ir=0.275 ))

#ARGS
def calcular_imposto_2(valor, *args): #chamar o "args" me permite passar quantos parâmetros de posição eu quiser - Pode ser qualquer coisa o nome ! O args é uma tupla   
      total_imposto = 0
      for item in args:
           total_imposto+= valor * item
      return total_imposto
      
print(calcular_imposto_2(1000, 0.275,0.05,0.0375,0.03))

#KWARGS - É UM DICIONÁRIO  
def calcular_imposto_trimestral(valor, **kwargs): #chamar o "kwargs" me permite chamar os parâmetros da mesma forma, só que, agora eu posso por o nome dos parâmetros para melhor identificar eles !    
      total_imposto = 0
      if "ir" in kwargs:
            total_imposto+= valor * kwargs['ir']
      if "csll" in kwargs:
            total_imposto+= valor * kwargs['csll']
      return total_imposto

print(calcular_imposto_trimestral(1000, ir=0.275, iss=0.05, csll=0.0375, p_is=0.03))



#Funções especiais

#Por padrão, argumentos podem ser passados para uma função tanto por porsição quanbto explicitamente pelo nome. 
#Para uma melhor lgibilidade e desempenho, faz sentido restringir a maneira pelo qual argumentos possam ser passados, assim um dev precisa
#apenas olhar para a definição da função para determinar se os itens são passados por posição, por posição e nome ou só por nome

# Temos o " apenas posicional"
#temos o apenas por nome (kwargs)
#Temos o hib´rido, keywords e posicional
