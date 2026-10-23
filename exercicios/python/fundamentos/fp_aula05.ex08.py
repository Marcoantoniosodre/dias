#Autor: Marco Antonio
#Projeto: Fatorial Ainda

numero= int(input('digite o seu numero '))
positivo= 0
negativo= 0
for i in range(10):
    numero= int(input(' digite o seu numero:  '))
    print(f'numero digitado: {numero} e o valor de {i}')
    if numero % 2 == 0:
        print(f' o numero {numero} é par')
    elif numero >0:
        positivo = positivo + 1
    elif numero <0:
        negativo = negativo +1
    else:
        print(f' o numero {numero} é impar')
print(f' o total de numeros pares foi de: {positivo}')
print(f' o total de numeros impares foi de: {negativo}')
print(f' o total de numeros positivos digitados foi de: {positivo}')
print(f' o total de numeros negativos digitados foi de: {negativo}')