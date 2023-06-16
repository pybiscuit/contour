import os
import sys
import math

import pygame as pg
from utils.settings import *

class App:

    def __init__(self, map_list, player, **kwargs):
        os.environ['SQL_VIDEO_WINDOW_POS'] = "%d, %d" % (50, 100)
        self.game_area = pg.display.set_mode(WIN_SIZE)
        self.clock = pg.time.Clock()
        self.map = map_list().gen_rects()
        self.map.reverse()
        self.player = player([(0,0,0), (640,384), 4, 0])
        self.entities = kwargs
        pg.init()
        self.font = pg.font.SysFont("Arial", FONT_SIZE)



    def check_event(self):
        pressed = pg.key.get_pressed()
        speed = 2.2
        if pressed[pg.K_LEFT]:
            self.player.update((-speed, 0))
        elif pressed[pg.K_RIGHT]:
            self.player.update((speed, 0))
        elif pressed[pg.K_DOWN]:
            self.player.update((0, speed))
        elif pressed[pg.K_UP]:
            self.player.update((0, -speed))

        for e in pg.event.get():
            if e.type == pg.QUIT or (
                e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            
    
    def update(self):
        for key in self.entities.keys():
            self.entities[key].update(events)

        self.dt = self.clock.tick() * 0.001
    
    def draw(self):
        # pygame.draw.ellipse(window, (255, 255, 255), ellipse_rect, 3)  

        interval = 255//60
        self.game_area.fill((255,255,255))
        for idx, rect in enumerate(self.map):
            # get the independant radii (pixel) of the ellipse
            a = rect.width // 2
            b = rect.height // 2

            # scale factor that is the ratio of radii
            scale_y = a / b

            # center (pixel) of the ellipse
            cpt_x, cpt_y = rect.center

            # check point pixel coordinates
            test_x, test_y = self.player.shape[1]

            # vector coods for player vector (origin at ellipse center)
            # scale factor used normalize ellipse to circle geometry.
            dx = test_x - cpt_x
            dy = (test_y - cpt_y) * scale_y

            collide = dx*dx + dy*dy >= a*a

            if idx > 0 and idx < len(self.map) - 1:
                prev = self.map[idx+1]

                pa = prev.width//2
                pb = prev.height//2

                pscale_y = pa/pb

                cpt_px, cpt_py = prev.center

                px = test_x - cpt_px
                py = (test_y - cpt_py) * pscale_y

                pcollide = px*px + py*py <= pa*pa
                if pcollide and collide:
                     pg.draw.ellipse(self.game_area, (187,25,78), rect, 0)
                elif collide:
                    pg.draw.ellipse(self.game_area, (0+(interval*idx),0+(interval*idx),0), rect, 0)
                elif not pcollide and not collide:
                    pg.draw.ellipse(self.game_area, (255,255,255), rect, 0)
                else:
                    pg.draw.ellipse(self.game_area, (0+(interval*idx)*(46/255),0+(interval*idx)*(139/255),0+(interval*idx)*(87/255)), rect, 0)

            else:
                if collide:
                    pg.draw.ellipse(self.game_area, (0+(interval*idx),0+(interval*idx),0), rect, 0)
                else:
                    pg.draw.ellipse(self.game_area, (255,255,255), rect, 0)
            
        
        line_end = (
            self.player.shape[1][0] + self.player.x*25,
            self.player.shape[1][1] + self.player.y*25
        )
  
        pg.draw.line(self.game_area, (255,0,0), self.player.shape[1], line_end, 3)
        pg.draw.circle(self.game_area, self.player.shape[0], self.player.shape[1], self.player.shape[2], self.player.shape[3])
        # pg.draw.line(self.game_area, (255,255,255), (self.player.shape[1][0],0), (self.player.shape[1][0], 768), 1)
        # pg.draw.line(self.game_area, (255,255,255), (0,self.player.shape[1][1]), (1280,self.player.shape[1][1]), 1)
        self.draw_fps()
        pg.display.flip()

    def draw_fps(self):
        fps = f'{self.clock.get_fps():.0f} FPS'
        self.game_area.blit(self.font.render(
            fps, (0,0), (0,0,0)), (10,0))
        
    def run(self):
        while True:
            self.check_event()
            self.update()
            self.draw()
            
            # debug_console = input("Enter stuff\n> ")
            # pg.draw.line(self.game_area, (0,0,0), (self.player.shape[1][0],0), (self.player.shape[1][0], 768), 1)
            # pg.draw.line(self.game_area, (0,0,0), (0,self.player.shape[1][1]), (1280,self.player.shape[1][1]), 1)
            # if debug_console == 'move_player':
            #     coords = input("enter player coords:")
            #     coords = [int(i) for i in coords.split(',')]
            #     self.player.update(coords)
            # elif debug_console == 'map':
            #     print(pg.draw.ellipse(self.game_area, (178,24,0), self.map[0], 1))
            #     pg.display.flip()
            #     input("")
            # elif debug_console == 'coords':
            #     print(f"{self.player.shape[1]}")
            # pg.display.flip()

