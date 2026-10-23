#Autor: Marco Antonio
#Usando o if, elif e else para certas condições

idade= int(input('digite sua idade aqui:'))

if idade > 18:
    print(' Acesso liberado')
elif idade < 18:
    print('Acesso negado, voce é menor de idade')
else:
    print('Seja bem vindo, voce tem exatamente 18 anos')

    # O código acima é um exemplo de uso do if, elif e else para verificar a idade do usuário e fornecer uma resposta adequada com base na condição. O programa solicita ao usuário que digite sua idade, e então verifica se a idade é maior, menor ou igual a 18 anos, respondendo de acordo.
    # O if é usado para verificar a primeira condição (idade > 18), o elif é usado para verificar a segunda condição (idade < 18), e o else é usado para lidar com a situação em que a idade é exatamente 18 anos.
