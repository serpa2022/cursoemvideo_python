
'''Programa para tocar áudio'''

#Importe biblioteca específica
import pygame
pygame.init()
pygame.mixer.music.load('estrangeiro.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()

