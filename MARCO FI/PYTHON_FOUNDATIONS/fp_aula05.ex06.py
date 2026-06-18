#Autor: Marco Antonio
#Desafio: fatorial

numero= int(input("Digite um número para calcular o fatorial: "))
fatorial= 1

for numero in range(1, numero+1):
    fatorial *= numero
    print(f'o resultado sera de: {fatorial}')

