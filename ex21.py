# programa para executar um arquivo MP3 em python, no entanto, é necessário que o arquivo de mp3 esteja na mesma pasta do programa.
import pygame

pygame.mixer.init()

pygame.init()

pygame.mixer.music.load('whatislove.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()
