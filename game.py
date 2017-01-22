import pygame
from map import *
from block import * # import all funcs from block.py

blocks = [];
blocks.append(Block('.', 1, 3, False))
blocks.append(Block('#', .5, 5, False))
blocks.append(Block("~", .1, 4, False))

class Game:
    # init initializes the map, the user, and the blocks
    def __init__(self):
        # init blocks
        self.map_ = Map(blocks)

    def run_game(self):

        time_down = 0.0
        time_elapsed = 0.0

        while True:
            for ev in pygame.event.get():
                if ev.type == QUIT:
                    break # you had a semicolon here, there is no need for it
                elif ev.type == KEYDOWN:
                    if ev.key == K_SPACE:
                        time_down = pygame.time.get_ticks()
                elif ev.type == KEYUP:
                    if ev.key == K_SPACE:
                        key += 1
                        time_elapsed = (pygame.time.get_ticks() - time_down)/1000.0
                        print("number: ", key, "duration: ", time_elapsed)

            self.tick()
            pygame.display.update()
