import sys
import pygame as pg

pg.init()
screen = pg.display.set_mode((800,800))
pg.display.set_caption("Pymon")
#experiment 

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()