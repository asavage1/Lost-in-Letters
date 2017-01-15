# map.py
# Andrew Savage
# map generation for lost in letters

#import game
from block import *
import random

class Map:
    global increment_height
    increment_height = 100#0
    global increment_width
    increment_width = 100#0
    global display_width
    display_width = 100
    global display_height
    display_height = 40
    global air
    air = ' ' # may want to change air to be a block type for consistency purposes
    global grass_std
    grass_std = 2
    
    def __init__(self, block_array): # intialize grass object?
        global blocks
        blocks = block_array
        self.quad_1 = [] # (0,0)
        self.quad_2 = [] # (-1,0)
        self.quad_3 = [] # (-1,-1)
        self.quad_4 = [] # (0,-1)
        expand_quad(self.quad_1)
        #expand_quad(self.quad_2)
        #expand_quad(self.quad_3)
        #expand_quad(self.quad_4)
        
    def move_player(self, pos):
        return 0

    def place_block(self, pos, block):
        return 0

    def destroy_block(self, pos, block):
        return 0

    # this needs to be broken up
    def print_(self, x, y):
        if x > display_width: # do not need to print quads 2 or 3
            if y > display_height: # only print quad 1
                print_one(self.quad_1[-1::-1], x, len(self.quad_1) - y)
            elif y < -display_height: # only print quad 4
                print_one(self.quad_4, x, y)
            else: # print quad 1 and 4
                print_vert(self.quad_1, self.quad_4)
        elif x < -display_width: # do not need to print quads 1 or 4
            if y > display_height: # only print quad 2
                print_one(horz_flip(self.quad_2)[-1::-1], len(self.quad_2[0]) - x, len(self.quad_2) - y)
            elif y < -display_height: # only print quad 3
                print_one(horz_flip(self.quad_3), len(self.quad_3[0]) - x, y)
            else: # print quad 2 and 3
                print_vert(horz_flip(self.quad_2), horz_flip(self.quad_3), len(self.quad_3[0]) - x, y)
        else:           
            if y > display_height: # 1 and 2
                print_horz(self.quad_1, self.quad_2, x, y) #FIX THIS ONE
            elif y < -display_height: # 3 and 4
                return 0
            else: # all 4
                return 0

########## Printing ##########
def print_one(quad, x, y):
    for i in range(y + display_height, y - display_height):
        print(quad[-i][x - display_width : x + display_width], end = '\n')

def print_vert(quad1, quad2, x, y):
    for i in range(y + display_height, -1, -1):
        print(quad1[i][x - display_width : x + display_width], end = '\n')

    for i in range(0, y - display_height, -1):
        print(quad2[-i][x - display_width : x + display_width], end = '\n')

def print_horz(quad1, quad2, x, y):
    for i in range(y - display_height, y + display_height):
        print(quad1[i][display_width - x : -1], end = '')
        print(quad2[i][0 : display_width + x], end = '\n')

def horz_flip(quad): # does not modify original array
    flipped = []
    for i in range(len(quad)):
        flipped.append(quad[i][-1::-1])
    return flipped
########## End Printing ##########

########## Expanding and Filling ##########
def expand_quad(quad):
    for x in range(increment_width):
        quad.append([])

    len_ = len(quad[0]) + increment_height
    for x in range(len(quad)):
        while (len(quad[x]) != len_):
            quad[x].append('')
    fill(quad)
    ##  testing map
    full_map = []
    for col in quad:
        elem_list = []
        for elem in reversed(col):
            if elem == air:
                elem_list.append(elem)
            else:
                elem_list.append(elem.get_skin())
        full_map.append(elem_list)
    for col in zip(*full_map):
        print(''.join(col))
    ##
        
def fill(quad):
    for col in quad:
        adj_grass = adj_grass_height(quad, col)
        grass_ht = grass_height(adj_grass)
        print("adj_grass: " + str(adj_grass) + " grass_ht: " + str(grass_ht))
        for height in range(len(col)):
            if col[height] == '':
                if height == grass_ht:
                    col[height] = blocks[0] # blocks[0] is grass
                elif height > grass_ht:
                    col[height] = air
                elif height < grass_ht:
                    col[height] = get_ground(height)

# fill helpers
def adj_grass_height(quad, col):
    # col and col-1 are both never None
    if col is None or quad[quad.index(col) - 1] is None:
        return 0 # defaults to 0
    col = quad[quad.index(col) - 1]
    #try catch (ValueError): # catching errors?
    return col.index(blocks[0])

def grass_height(adj_grass):
    return max(int(random.normalvariate(adj_grass, grass_std)), 0)

# TODO: make rarity more uniform as height gets smaller -- population growth model?
def get_ground(height):
    population = []
    weights = []
    for block_index in range(1,len(blocks)): # excludes grass
        population.append(blocks[block_index])
        weights.append(blocks[block_index].get_rarity())
    return random.choices(population, weights)[0]
########## End Expanding and Filling ##########
