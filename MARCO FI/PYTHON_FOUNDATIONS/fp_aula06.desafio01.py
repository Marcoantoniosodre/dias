#Autor Marco Antonio
#Desafio: Fatorial usando while

numero= int(input("Digite um número para calcular o fatorial: "))
fatorial= 1
i= 1

while i <= numero:
    fatorial *= i
    print(f' o resultado sera de: {fatorial}')
    i= i+1
 