import pygame as pg
from utils.settings import *
import sys
import os
from math import pi

# lazer beam pg.Rect(600-i*10, 364-i*10, 40+i*2, 20+i*2) for i in range(60)



class ContourMap:

    def __init__(self):
        self.el_rects = self.gen_rects()
    
    def gen_rects(self):

       return [
           pg.Rect(635-i*10, 379-i*10, 20+i*20, 10+i*20) for i in range(60)
           ]
        # pg.draw.arc(self.game_area, (0,0,0), pg.Rect(620,344, 40, 40),pi/100, (11*pi)/6, 1)

    

    

