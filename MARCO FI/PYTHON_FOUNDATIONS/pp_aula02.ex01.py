#Autor: Marco Antonio
#Entendendo funções e onde aplica 

def calcular (opala, chevette, mecanico):
    return eval (f'{opala} {mecanico} {chevette}')

n1= float(input( 'Digite o primwiro valor: '))
n2= float(input( 'Digite o segundo valor:  '))
op= input( 'Digite a opercação: [ + - * /]')
print(' o resultado é: ', calcular(n1, op, n2))