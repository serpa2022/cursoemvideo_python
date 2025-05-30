
'''Programa para calcular seno, cosseno e tangente'''

import math

#Digite o valor do ângulo desejado:
ang = float(input('Digite o ângulo que você deseja: '))

#Cálculo do seno:
seno = math.sin(math.radians(ang))
 
 #Cálculo do cosseno:
cosseno = math.cos(math.radians(ang))

#Cálculo da tangente:
tangente = math.tan(math.radians(ang))

#Calcule o resultado das operações:
print(f'O ângulo de {ang} tem o SENO de {seno:.2f}')
print(f'O ângulo de {ang} tem o COSSENO de {cosseno:.2f}')
print(f'O ângulo de {ang} tem a TANGENTE de {tangente:.2f}')
 
