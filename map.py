# map.py
# Andrew Savage
# map generation for lost in letters
import game
import block
import random
class Map:
    increment_height = 1000
    increment_width = 1000
    display_width = 100
    display_height = 40
    air = ' '
    def __init__(self):
        self.quad_1 = [] # (0,0)
        self.quad_2 = [] # (-1,0)
        self.quad_3 = [] # (-1,-1)
        self.quad_4 = [] # (0,-1)
        expand_quad(self.quad_1)
        expand_quad(self.quad_2)
        expand_quad(self.quad_3)
        expand_quad(self.quad_4)

    def expand_quad(quad):
        for x in range(increment_width):
            quad.append([])

        len_ = len(quad[0] + increment_height)
        for x in range(len(quad)):
            while (len(quad[x]) != len_)
                quad[x].append('')  
    def move_player(self, pos):

    def place_block(self, pos, block):

    def destroy_block(self, pos, block):



##### TESTING #####
# zip(*A) transposes matrix A
generateMap()
for col in zip(*Lmap):
    print(''.join(col))
for row in zip(*Rmap):
    print(''.join(col))
    
#print(Lmap)
#print(Rmap)
