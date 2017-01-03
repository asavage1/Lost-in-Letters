# map.py
# Andrew Savage
# map generation for lost in letters

# Global variables for display size
dispWidth = 30
disHeight = 30
initWidth = dispWidth * 10    # this is actually the initial width - 1
initHeight = dispHeight * 10

# Global variables for terrain sizes
skyHeight = 100

###### Global character vars (temporary) ######
sky = ' '
dirt = '#'
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
    for x in range(initWidth / 2):
        Rmap.append([])
        Lmap.append([])
    for x,y in map(None, Rmap, Lmap) # may have to do a less fancy way
        for z in range(initHeight):
            # Initialize all elements in map to ''
            x.append('')
            y.append('')

    # Initialize elements of array:
    #    1. Initialize sky (spaces)
    #    2. Initialize surface layer
    #    3. Initialize other layers (TBD)
    #    4. Initialize special objects (Later versions)
    #
    # Use normal distribution for surface layer?
    for x, y in map(None, Rmap, Lmap):
        for z in range(skyHeight):
            x[z] = sky
            y[z] = sky
        x[skyHeight] = grs
        y[skyHeight] = grs
        for z in range (skyHeight + 1, initHeight):
            x[z] = grnd
            y[z] = grnd

    
# generateMap helpers


    
##### Expand Map #####

# Expand map when player goes outside of generated range
def expandMap(): # Pass character coordinates?
    # Add a chunk, size determined by global vairables
    
