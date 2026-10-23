#Autor: Marco Antonio
#Projeto: desafio 



numero= int(input('digite o seu numero '))
contador= 0

for i in range(10):
    numero= int(input(' digite o seu numero:  '))
    print(f'numero digitado: {numero} e o valor de {i}')
    if numero >0:
        contador = contador + 1
        if numero <0:
            contador = contador +1  
print(f' o total de numeros positivos digitados foi de: {contador}')
print(f' o total de numeros negativos digitados foi de: {contador}') 
