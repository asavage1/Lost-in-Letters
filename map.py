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
            while (len(quad[x]) != len_)
                quad[x].append('')
        fill(quad)
    def move_player(self, pos):

    def place_block(self, pos, block):

    def destroy_block(self, pos, block):

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
        for b in blocks:
            population.append(b.get_skin())
            weights.append(b.get_rarity())
        return random.choice(population, weights)
