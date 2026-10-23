# Autor: Marco Antonio
# tarefinha basica de descobrir a hipotenusa 
# potencia

oposto= float(input( ' digite o valor do oposto'))
adjacente= float(input(' digite o valor do adjacente'))

hipotenusa= (oposto ** 2 + adjacente ** 2 ) ** 0.5

# exibir o numero formatado com duas casas decimais
print(f'o valor da hipotenusa sera de: {hipotenusa:.2f}') 

#round()
# hipotenusa = round( hipotenusa, 2)
# seve para arredondar a quantidade de casas que queremos 

hipotenusa = round(hipotenusa,)
print(f'O valor da hipotenusa sera de; {hipotenusa}' )



# Usando o round

valor= float(int(' Valor em reais'))
valor2= float(int( 'valor em dolar'))

resultado = valor/valor2

resultado = round(resultado,)

print(f' o resultado sera de: {resultado:.2f }')
