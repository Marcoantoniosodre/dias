#Autor: Marco Antonio
#Dicionarios na pratica 

def calcular (a, b, op):
    operacoes = {
        '+': a + b,
        '-': a - b,
        '*': a * b,
        '/': a / b,
        '%': a % b,
        '**': a ** b,
        '//': a // b
    }
    return operacoes [op]
n1= float(input( 'Digite o primeiro valor: '))
n2= float(input( 'Digite o segundo valor:  '))
op= input( 'Digite a opercação: [ + - * / % ** //]: ')

print(calcular(n1, n2, op))