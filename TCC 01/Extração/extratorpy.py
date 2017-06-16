# -*- coding: UTF-8 -*-
import numpy as np
import pandas

# - Global (global nomeVariavel)
tes = pandas.read_csv("./tabula-01-jan-17.csv")
lista = []
teste = []
entidades = [
				"LOCAL:", "SUSPEITO:", "VEÍCULO:", "VÍTIMA:", "VÍTIMAS:", "VÍTIMA FATAL:", "ARMA APREENDIDA:",
				"MATERIAL APREENDIDO:", "PLACA:", "VÍTIMAS LESIONADAS:", "OBJETOS"
			]

# - Tirando as outras 2 colunas
del tes['FONTE']
del tes['NATUREZA DA OCORRÊNCIA']


#for i in tes.iterrows():
#	print (i)

# - Salva em 'lista' as linhas de HISTÓRICO DA OCORRÊNCIA
for i, row in tes.iterrows():
	if row['HISTÓRICO DA OCORRÊNCIA']:
		lista.append(tes.loc[i,:])

# - Salva em 'teste' as linhas de 'lista'
for k in lista:
	#print (k.values)
	teste.append(k.values)

# - Teste da quantidade de linhas
#print(len(teste))
#print(type(teste[0]))

#for l in teste[0]:
#	print (l)

def excluirTextoDaString(string, inicio, fim):
	pass

def transformaListEmString(lista):
	aux = ""
	for strCelula in lista:
		for strIterator in strCelula:
			aux += strIterator
	return aux

def extrair(string, inicio, entidade):
	aux = ""
	
	# - Início real da função de extração
	# - Precisa fazer o processo de excluir da string os dados retornados aqui
	i = inicio;
	while i < len(string):
		if (string[i] != "."):
			aux += string[i]
		if (string[i] == "."):
			break
		i += 1

	# - Depois usar um 'return' ao invés de só imprimir
	print (entidade + " " + aux)


# Recebe a string completa de uma linha do HISTÓRICO DA OCORRÊNCIA
def extrairEntrePontos(string):
	i = 0;
	while i < len(string):
		# - Se encontrar dois pontos chamar 'extrair()' passando a string e a posição que deve começar a extrair
		# - Essa função sempre começa lendo do início da string 'stringLinha', portanto só pega o primeiro ':' e '.'
		if (string[i] == ":"):
			extrair(string, i+2) #Pegar o tamanho dos espaços
			break
		i += 1


# - Função para retirar espaços do início da string que irá ser extraída. Depois tratar caso de dois pontos ':'
def tirarEspacosDoInicio(string, inicio):
	
	inicioDaString = inicio
	if (string[inicioDaString] == " "):
		while (string[inicioDaString] == " "):
			inicioDaString = inicioDaString+1
	return inicioDaString


# - Extrai uma entidade, porém tem que tratar o caso de quando a entidade não existe
def extrairUmaEntidade(teste, entidade):
	t = 0
	while t < len(teste):
		stringLinha = transformaListEmString(teste[t])
		print (stringLinha)

		posicaoIni = stringLinha.find(entidade)

		if (posicaoIni == -1):
			print (entidade + " NÃO POSSUI ESSA INFORMAÇÃO")
		else:
			posicaoIni = posicaoIni + len(entidade)
		
			posicaoIni = tirarEspacosDoInicio(stringLinha, posicaoIni)

			extrair(stringLinha, posicaoIni, entidade)
		t += 1

# - Extrai uma entidade, porém tem que tratar o caso de quando a entidade não existe
def extrairUmaEntidadeEmUmaLinha(teste, entidade, posicao):
	# - teste[posicao] é do tipo narray, e anteriormente list, por isso, para facilitar, é feito a conversão para string
	stringLinha = transformaListEmString(teste[posicao])
	print (stringLinha + "\n")

	posicaoIni = stringLinha.find(entidade)

	if (posicaoIni == -1):
		print (entidade + " NÃO POSSUI ESSA INFORMAÇÃO")
	else:
		posicaoIni = posicaoIni + len(entidade)
	
		# - Tira os espaços desnecessários do início da string
		posicaoIni = tirarEspacosDoInicio(stringLinha, posicaoIni)

		extrair(stringLinha, posicaoIni, entidade)


# - Extrai todas entidades, porém tem que tratar o caso de quando a entidade não existe
def extrairTodasEntidades(teste):
	t = 0
	while t < len(teste):
		# - teste[t] é do tipo narray, e anteriormente list, por isso, para facilitar, é feito a conversão para string
		stringLinha = transformaListEmString(teste[t])
		print (stringLinha  + "\n")

		for entidade in entidades:
			posicaoIni = stringLinha.find(entidade)

			if (posicaoIni == -1):
				print (entidade + " NÃO POSSUI ESSA INFORMAÇÃO")
			else:
				posicaoIni = posicaoIni + len(entidade)

				# - Tira os espaços desnecessários do início da string
				posicaoIni = tirarEspacosDoInicio(stringLinha, posicaoIni)

				extrair(stringLinha, posicaoIni, entidade)
		print ("\n")
		t += 1


#extrairEntrePontos(stringLinha)

# - Faz o processo de extração
#extrair(stringLinha, posicaoIni)

#extrairUmaEntidade(teste, "SUSPEITO:")

extrairTodasEntidades(teste)

#extrairUmaEntidadeEmUmaLinha(teste, "ARMA APREENDIDA:", 10)
