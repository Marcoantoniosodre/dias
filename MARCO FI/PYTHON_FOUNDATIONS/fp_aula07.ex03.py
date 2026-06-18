#Autor: Marco Antonio
#Projeto: funções LISTAS

alunos= [ 'enzo', 'marco', 'jose', 'maria', 'ana', 'lucas', 'carla', 'roberto', 'fernanda', 'ricardo']
print(f' a lista de alunos no inicio foi de: {len(alunos)}, sendo eles: {", ".join(alunos)}')
print()
alunos.remove('jose')
alunos.remove('fernanda')
print(f'Os alunos jose e fernanda foram desligados do curso, então a lista de alunos no final foi de: {len(alunos)}, sendo eles: {", ".join(alunos)}')
print()
alunos.insert(0, 'carlos')
alunos.insert(3, 'julia')
print(f'2 pessoas entraram, sendo eles o carlos e a julia, então a lista de alunos no final foi de: {len(alunos)}, sendo eles: {", ".join(alunos)}')
print()
alunos.sort()
print(f'O curso finalizou com essa lista de alunos no final foi de: {len(alunos)}, sendo eles: {", ".join(alunos)}')