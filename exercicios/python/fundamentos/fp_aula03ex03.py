#Autor: Marco Antonio
#Cauculo de imc

peso= float(input( ' digite teu peso aqui:'))
altura= float(input( 'digite sua altura aqui:'))

imc= peso / (altura**2 )

print(f'Seu imc é de: {imc:.2f}')

if imc <= 18.5:
    print(' voce é magrelo KKKKKK')
elif imc <= 24.9:
    print(' voce é normal, boa cria')
elif imc <= 29.9:
    print(' ta começando a fica gigatesco em bola')
elif imc <= 34.9:
    print(' O CARA TA FICANDO GORDAAASSOO')
elif imc <= 39.9:
    print(' ta obeso ja, nivel 2 ')
else:
    print(' OBESIDADE MOOORBIDA, SEU KOMBI DO CARAMBA KKKKKK')

#primeira parte do código é o calculo do imc, usando a formula peso/altura**2
#segunda parte do código é a classificação do imc usando estruturas condicionais (if, elif  e else) 
# o resultado do imc é formatado para mostrar apenas 2 casas decimais usando :.2f dentro da f-string