from block import *
from map import *

blocks = []
blocks.append(Block('_', 0, 3, False)) # grass
blocks.append(Block('#', 1, 3, False)) # temp ground

game_map = Map(blocks)
