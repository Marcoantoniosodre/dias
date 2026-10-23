#Autor: Marco Antonio
# extrutura condicional  

nota1 = float(input( ' Digite a primeira nota do aluno: '))
nota2 = float(input( ' Digite a segunda nota do aluno: '))
nota3 = float(input( ' Digite a terceira nota aluno: '))
nota4 = float(input( ' Digite a quarta nota aluno: '))
media= (nota1+nota2+nota3+nota4) / 4

print(f'A nota do aluno é: {media:.1f}')

if media >= 5:
    print (' Aluno Aprovado!!')
else:
    print (' Aluno Reprovado!!')
