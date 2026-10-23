#autor: Marco
#projeto calculadora com recebimentos de dados do usuario


valor1= int (input('digite o primeiro valor:'))

valor2= int (input('digite o segundo valor:'))

#variavel do tipo "int" é relativa a valores inteiros 
# a palavra reservada "input" é usada para receber dados do usuario 
soma= valor1 + valor2 


print(' a soma sera de ',soma) 
#para fazer um texto dentro de um print precisa de aspas,sendo simples ou dupla 
#variavel NAO ENTRA EM ASPAS 


# print formatado, usando f-string 
print(f'o resultado da soma é: {soma}') 