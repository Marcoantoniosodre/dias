#Autor: Marco Antonio
#Palhaçada 
def soma():
       v1= float(input('Digite o primeiro valor: '))    
       v2= float(input('Digite o segundo valor:'))
       soma = v1 + v2
       return soma
def subtracao():
       v1= float(input('Digite o primeiro valor: '))
       v2= float(input('Digite o segundo valor: '))
       subtracao = v1 - v2 
       return subtracao
def multiplicacao():
       v1= float(input('Digite o primeiro valor: '))
       v2= float(input('Digite o segundo valor: '))
       multiplicacao = v1 * v2
       return multiplicacao
def divisao():
       v1= float(input('Digite o primeiro valor: '))
       v2= float(input('Digite o segundo valor: '))
       divisao = v1 / v2
       return divisao

print('Bem vindo a palhaçada')
print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')
opcao = int(input('Digite a opção desejada: '))
if opcao == 1:
       print(soma())
elif opcao == 2:
       print(subtracao())
elif opcao == 3:
       print(multiplicacao())
elif opcao == 4:
       print(divisao())
else:
       print('Opção inválida, palhação')
