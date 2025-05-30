
'''Programa para calcular o gasto de aluguel de carros'''

#Leia a quantidade de dias alugados:
dias = int(input('Quantos dias alugados? '))

#Leia a quantidade de quilômetros rodados:
km = float(input('Quantos km rodados? '))

#Cálculo do preço do aluguel do carro:
preco = (dias*60)+(km*0.15)

#Escreva o valor final do aluguel:
print(f'O total a pagar é de R${preco:.2f}')
