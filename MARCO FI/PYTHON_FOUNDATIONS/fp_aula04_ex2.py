#Marco Antonio

#exercicio de acessos 

usuario= 'marco'
idade= 18

credencial_usuario= input("Digite seu nome de usuario: ")
idade_usuario= int(input("Digite sua idade: "))

if idade_usuario== idade and credencial_usuario== usuario: 
    print(f' Bem vindo, {credencial_usuario} ') 
elif idade_usuario == idade and credencial_usuario != usuario:
    print(' Usuario incorreto, acesso negado ')
elif idade_usuario != idade and credencial_usuario == usuario:
    print(' idade incorreta, acesso negado ')
else:   print(' Usuario e idade incorretos, acesso negado ')