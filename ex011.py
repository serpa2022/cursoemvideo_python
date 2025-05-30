
'''Programa para calcular a quantidade de tinta necessária pra pintar a área de uma parede'''

#Variáveis com valores da altura e largura da parede

alt = float(input('Digite a altura da parede: '))
lar = float(input('Digite a largura da parede: '))

#Variável contendo o valor da área da parede

area=alt*lar

#Escreva o valor da área da parede

print(f'As dimensões da parede são de {alt}m e {lar}m e a área é de {area}m²')

#Variavel para calcular a quantidade de tinta, sabendo que 1 lata de tinta pinta 2m²

tinta=area/2

#Escreva a quantidade de tinta necessária, revelando o valor da área

print(f'Para pintar essa parede você vai precisar de {tinta} litros')
