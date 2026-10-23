
#Autor Marco 
# exercicio de AND, OR e ! parte 2

bafometro= 'sim'
carteira= 'sim' 


bafometro_teste= input(' resultado do bafometro:')
carteira_motorista_teste= input(' voce tem a carteira de motorista? ')

if bafometro_teste == bafometro and carteira_motorista_teste == carteira:
    print(' voce esta alcoolizado, toma multa e nao pode seguir')
elif bafometro_teste != bafometro and carteira_motorista_teste == carteira:
    print(' voce pode seguir, vai na paz ') 
elif bafometro_teste == bafometro and carteira_motorista_teste != carteira:
    print(' voce ta bebado e nao tem carteira, vai ver o sol nascer quadradooo')
