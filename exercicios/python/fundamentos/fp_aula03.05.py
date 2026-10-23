#Autor: Marco Antonio
# exercicio de AND, OR e !=

usuario = 'aluno'
senha = 'senha_de_exemplo'
acesso_usuario = input(' Digite o nome do usuario: ')
acesso_senha = input(' Digite a senha: ')

if acesso_usuario == usuario and acesso_senha == senha:
    print(f' Bem vindo, {acesso_usuario} ')
elif acesso_usuario != usuario and acesso_senha == senha:
    print(' Usuario incorreto, acesso negado ')
elif acesso_usuario == usuario and acesso_senha != senha:
    print(' Senha incorreta, acesso negado ')
else:    print(' Usuario e senha incorretos, acesso negado ')
