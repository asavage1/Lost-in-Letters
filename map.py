# map.py
# Andrew Savage
# map generation for lost in letters

import random

# Global variables for display size
dispWidth = 30
dispHeight = 30
initWidth = dispWidth * 10    # this is actually the initial width - 1
initHeight = dispHeight * 10

# Global variables for terrain sizes
skyHeight = int(initHeight / 3)

###### Global character vars (temporary) ######
sky = ' '
dirt = ['#','X']
grs = '_'

# Contains list of arrays which contain the ASCII chars in the map (in cols)
Rmap = [] # starts as 151 cols by 300 rows, includes center column
Lmap = [] # starts as 150 cols by 300 rows

##### Generate Map #####

# Run all processes to generate intial map
def generateMap():
    # Declare 2d array for map: Option 1: One 2d array that can expand any
    #                                     way but up
    #                                  2: 2 2d arrays that can expand only 2
    #                                     ways, both expand down, the left
    #                                     one expands "left" and the right
    #                                     one expands "right"
    # Option 1 may make it hard to keep track of player coordinates
    Rmap.append([]) # center column
    for x in range(int(initWidth / 2)):
        Rmap.append([])
        Lmap.append([])
    # Can combine these two pieces
    for x in Rmap:
        for y in range(initHeight):
            x.append('')
    for x in Lmap:  
        for y in range(initHeight):
            x.append('')

    # Initialize elements of array:
    #    1. Initialize sky (spaces)
    #    2. Initialize surface layer
    #    3. Initialize other layers (TBD)
    #    4. Initialize special objects (Later versions)
    #
    # Use normal distribution for surface layer?
    # Can combine these two pieces
    i = 1
    for x in Rmap:
        for y in range(skyHeight):
            x[y] = sky
        x[skyHeight] = grs
        for y in range (skyHeight + 1, initHeight):
            x[y] = random.choice(dirt)
    for x in Lmap:
        for y in range(skyHeight):
            x[y] = sky
        x[skyHeight] = grs
        for y in range (skyHeight + 1, initHeight):
            x[y] = random.choice(dirt)
        i = i + 1
        if i % 1000:
            random.seed();

    
# generateMap helpers


    
##### Expand Map #####

# Expand map when player goes outside of generated range
def expandMap(): # Pass character coordinates?
    # Add a chunk, size determined by global vairables
    x = 0 #temp
    

##### TESTING #####
# zip(*A) transposes matrix A
generateMap()
for col in zip(*Lmap):
    print(''.join(col))
for row in zip(*Rmap):
    print(''.join(col))
    
#print(Lmap)
#print(Rmap)
