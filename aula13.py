nome = 'Inaldo Monteiro'
altura = 1.80
peso = 120
imc = peso / (altura * altura) #IMC = peso / (altura x altura)


print( nome, 'tem', altura, 'de altura' )
print( 'pesa', peso, 'quilos')
print('Seu imc é:', imc)

#Luiz Otávio tem 1.80
#pesa 95 quilos e seu IMC é
#29.3209

linha = f'{nome} tem {altura} de altura e {peso} quilos e seu imc é {imc:.2f}'
print(linha)