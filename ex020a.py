
'''Programa para sortear a ordem dos alunos'''

#Importando biblioteca
import random

#Digite o nome dos estudantes
a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))

#Apresentação da lista
lista = [a1, a2, a3, a4]

#Módulo para embaralhar lista
random.shuffle(lista)

#Exibir a ordem de apresentação depois do embaralhamento
print(f'A ordem de apresentação será: {lista}')