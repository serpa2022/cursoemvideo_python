
'''Programa para sortear um dos nomes de alunos digitados'''

#Importar biblioteca que sorteia dados
from random import choice 

#Digita o nome dos alunos:
aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))

#Escreva nome do aluno sorteado
print(f'O aluno escolhido foi {choice([aluno1, aluno2, aluno3, aluno4])}')