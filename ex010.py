
'''Programa para converter reais em dólares'''

#Leia a quantidade de reais que tem na carteira

d = float(input('Digite quanto de reais você tem na carteira: '))

#Escreva quantos dólares você pode comprar

print(f'Com R${d:.2f} reais, você pode comprar US${d/3.27:.2f} doláres!')
