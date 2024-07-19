import sys
import pygame
#import scikit-learn as scik
#import tkinter as tk

pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Pymon")


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()