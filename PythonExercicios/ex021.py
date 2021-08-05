# pip install pygame
import pygame
pygame.init()
pygame.mixer.music.load('example.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input()