
'''Programa de conversão de temperatura'''

#Leia a temperatura em graus Celsius

celsius = float(input('Qual a temperatura em °C? '))

#Cálculo da conversão de Celsius para Fahrenheit

fahrenheit = celsius*1.8 + 32

#Cálculo do valor da temperatura em Kelvin

kelvin = celsius + 273

#Escreva a nova temperarura convertida

print(f'A temperatura de {celsius}°C corresponde a de {fahrenheit:.2f}F')
print(f'A temperatura de {celsius}°C corresponde a de {kelvin}K')
