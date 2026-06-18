# Autor: Marco Antonio
# Projeto desafio 01 - ETANO OU GASOLINA

"""
a empresa ABC deseja melhora seu consumo com os carros 
a empresa deseja inicialmente analisar o desempenho dos carros

a empresa precisa saber se conpensa abastecer com ETANOL ou GASOLINA

dados devem ser apresentados da seguinte forma:
nome da empresa_carro_combustivel_consumo
formatados com 2 casas decimais 
"""

gasolina= 6.69
etanol= 4.61

resultado = etanol/gasolina 

kilometros= float(input(' digite a kilometragem aqui:')) #km rodados
preço= float(input(' digite o valor do preço aqui:')) #preço da gasolina 

conta= kilometros/preço

if resultado > 0.7:
    print(' o mais vantajoso é a gasolina')
else:
    print('o mais vantajoso sera a etanol')

    print( resultado )
print('ABC', 'POLO TURBO DO JOSE ANGELO', 'KMS RODADOS', sep='_')
print(conta) 
