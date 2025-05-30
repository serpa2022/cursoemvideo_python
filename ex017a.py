
'''Programa para calcular a hipotenusa de um triângulo retângulo'''

from math import hypot

#Leia o comprimento do cateto oposto:
cat_oposto = float(input('Comprimento do cateto oposto: '))

#Leia o comprimento do cateto adjacente:
cat_adjacente = float(input('Comprimento do cateto adjacente: '))

#Escreva o cálculo da hipotenusa:
print(f'A hipotenusa vai medir{hypot(cat_oposto, cat_adjacente):.2f}')


