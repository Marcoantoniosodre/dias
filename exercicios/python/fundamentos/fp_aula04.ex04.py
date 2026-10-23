#Autor: Marco Antonio
# Palhaçada com desconto e porcentagem

valor= 250
desconto= 0.15
valor_final= (1-desconto)*valor
if desconto == "sim":
    print(f' o desconto sera de: {valor_final}')
else:   print(f' o valor a ser pago sera de: {valor_final}')
