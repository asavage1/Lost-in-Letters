# map.py
# Andrew Savage
# map generation for lost in letters
#import game
import block
import random
class Map:
    increment_height = 1000
    increment_width = 1000
    display_width = 100
    display_height = 40
    air = ' '
    grass_std = 3
    def __init__(self): # intialize grass object?
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
            while (len(quad[x]) != len_):
                quad[x].append('')
        fill(quad)
        
    def move_player(self, pos):
        return 0

    def place_block(self, pos, block):
        return 0

    def destroy_block(self, pos, block):
        return 0

    def fill(quad):
        for col in quad:
            for height in range(len(col)):
                if col[height] == '':
                    adj_grass = adj_grass_height(quad, col)
                    grass_height = grass_height(adj_grass)
                    if height == grass_height:
                        # can't use self?
                        col[height] = self.blocks[0] # blocks[0] is grass
                    elif height > grass_height:
                        col[height] = air
                    elif height < grass_height:
                        col[height] = get_ground(height)

    # fill helpers
    def adj_grass_height(quad, col):
        if col is None:
            return 0 # defaults to 0
        col = quad[quad.index(col) - 1] # error checking
        return col.index(blocks[0].get_skin())

    def grass_height(adj_grass):
        return random.normalvariate(adj_grass, grass_std)

    # TODO: make rarity more uniform as height gets smaller -- population growth model?
    def get_ground(height):
        population = []
        weights = []
        for block_index in range(1,len(blocks)): # excludes grass
            population.append(blocks[block_index].get_skin())
            weights.append(blocks[block_index].get_rarity())
        return random.choices(population, weights)

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

            else: # all 4

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
