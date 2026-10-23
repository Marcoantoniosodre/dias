#Autor: Marco Antonio
#Projeto: Tres tabuadas com while 

v1= int(input('digite o numero da tabuada que deseja:  '))
v2= int(input('digite o numero da tabuada que deseja:  '))
v3= int(input('digite o numero da tabuada que deseja:  '))


print(f'\ntabuadas de {v1}, {v2} e {v3}\n')

linha=1

while linha <= 10:
    print(f'{v1} x {linha:2d} = {v1 * linha:2d} \t {v2} x {linha:2d} = {v2 * linha:2d} \t {v3} x {linha:2d} = {v3 * linha:2d}')
    linha= linha + 1
