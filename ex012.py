
'''Programa pra calcular preço de produto com desconto'''

#Leia o preço do produto antes do desconto

preco = float(input('Digite o preço de um produto: R$'))

#Desconto dado em cima do preço do produto

desc = preco*0.05

#Escreva o desconto do preço do produto

print(f'O produto que custava R${preco} terá um desconto de 5%')
print(f'e passará a custar {preco - desc:.2f}')
