import pygame as pg
import os
from enum import Enum

class Keys:
    class Attack_Keys(Enum):
        a = pg.K_a
        s = pg.K_s
        d = pg.K_d
        f = pg.K_f
        g = pg.K_g #probably melee attacj

    class Item_Key(Enum):
        c = pg.K_c #in battle crystal use
        b = pg.K_b
        q = pg.K_q
        w = pg.K_w
        e = pg.K_e
        r = pg.K_r #instant raft 

    class Menu_Key(Enum):
        m = pg.K_m

    class Direction_Keys(Enum):
        up = pg.K_UP
        down = pg.K_DOWN
        left = pg.K_LEFT
        right = pg.K_RIGHT

    class Confirm_Cancel(Enum):
        enter = pg.K_RETURN
        back_space = pg.K_BACKSPACE
