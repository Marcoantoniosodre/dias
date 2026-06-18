#Autor: Marco Antonio
#Projeto: Loop For - Tabuada  




while True:
     num = int(input('digite o numero da tabuada que deseja:  '))
     for i in range(1,11):
          print(f"{num} x {i} = {num * i}")

     denovo= input(' deseja calcular outra tabuada? (s/n): ')
     if denovo.lower() != 's':
          print('obrigado por usar a tabuada do marco, volte sempre!')
          break