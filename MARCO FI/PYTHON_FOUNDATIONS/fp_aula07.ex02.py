#Autor: Marco Antonio
#Projeto: funções LISTAS

filmes= [' jujutsu kaisen', ' dragonball super', ' naruto shippuden', ' one piece', ' attack on titan']
print(filmes)
print(filmes[2])

filmes.append( ' death note')
print(filmes)
#o insert permite inserir um elemento em uma posição específica da lista, sem substituir o elemento existente nessa posição.
filmes.insert(2, ' hunter x hunter')
print(filmes)
#sort ordena a lista em ordem alfabética
filmes.sort()
#o join é um método de string que permite concatenar os elementos de uma lista em uma única string, usando um separador especificado entre os elementos.
print(' | ' .join(filmes))
# o * serve para desempacotar a lista, ou seja, para imprimir cada elemento da lista separadamente, em vez de imprimir a lista inteira como um único objeto.
print(*filmes, sep= ' | ' )