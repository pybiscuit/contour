import pygame as pg
from utils.settings import *
import sys
import os
from math import pi

# lazer beam pg.Rect(600-i*10, 364-i*10, 40+i*2, 20+i*2) for i in range(60)



class ContourMap:

    def __init__(self):
        self.rects = self.gen_rects()
    
    def gen_rects(self):

       return [
           pg.Rect(635-i*10, 379-i*10, 20+i*20, 10+i*20) for i in range(60)
           ]
        # pg.draw.arc(self.game_area, (0,0,0), pg.Rect(620,344, 40, 40),pi/100, (11*pi)/6, 1)

    def update(self, player_coords):
        for idx, rect in enumerate(self.rects):
            # get the independant radii (pixel) of the ellipse
            a = rect.width // 2
            b = rect.height // 2

            # scale factor that is the ratio of radii
            scale_y = a / b

            # center (pixel) of the ellipse
            cpt_x, cpt_y = rect.center

            # check point pixel coordinates
            test_x, test_y = player_coords

            # vector coods for player vector (origin at ellipse center)
            # scale factor used normalize ellipse to circle geometry.
            dx = test_x - cpt_x
            dy = (test_y - cpt_y) * scale_y

            collide = dx*dx + dy*dy >= a*a


            if idx > 0 and idx < len(self.rects) - 1:
                prev = self.map.rects[idx+1]

                pa = prev.width//2
                pb = prev.height//2

                pscale_y = pa/pb

                cpt_px, cpt_py = prev.center

                px = test_x - cpt_px
                py = (test_y - cpt_py) * pscale_y

                pcollide = px*px + py*py <= pa*pa
            
    

    

