#Autor: Marco Antonio
#Projeto: funções LISTAS


#Listas são estruturas de dados que permitem armazenar múltiplos valores em uma única variável. Elas são mutáveis, o que significa que seus elementos podem ser alterados após a criação da lista. As listas são definidas usando colchetes [] e os elementos são separados por vírgulas.
nomes= ['Marco', 'Enzo', 'Marcelo', 'Jose','Goku']
print(nomes)
print(nomes[2])

#As listas em Python são indexadas, o que significa que cada elemento tem um índice associado a ele. O índice começa em 0 para o primeiro elemento, 1 para o segundo, e assim por diante. Você pode acessar os elementos da lista usando esses índices.
nomes[3] = 'Vegeta'
print(nomes)

#As listas em Python são mutáveis, o que significa que você pode alterar seus elementos após a criação da lista. Você pode adicionar, remover ou modificar os elementos da lista conforme necessário.
nomes.append('Luffy')
print(nomes)

nomes.remove('Luffy')
print(nomes)