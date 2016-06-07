# Define an empty Tile class


#################################################
# Student adds code where appropriate

# imports
import simplegui

# globals
TILE_WIDTH = 50
TILE_HEIGHT = 100

# definition of empty Tile class (use pass in the body)
class Tile():

    # definition of initializer
    def __init__(self, num, exp, pos):
        self.number = num
        self.exposed = exp
        self.tile_position = pos

    # a string that returns the state of the objects
    def __str__(self):
        if self.exposed == True:
            return "The value of the tile is " + str(self.number) + " and the tile is exposed."
        else:
            return "The value of the tile is " + str(self.number) + " and the tile is NOT exposed."

    # return number of Tile
    def get_number(self):
        return num

    # return the value of exposed
    def is_exposed(self):
        return self.exposed

    # set value of exposed to true
    def expose_tile(self):
        self.exposed = True

    # set value of exposed to false
    def hide_tile(self):
        self.exposed = False

    # draw tile
    def draw_tile(self, canvas):
        pass

# draw handler
def draw(canvas):
    tile1.draw_tile(canvas)
    tile2.draw_tile(canvas)


# create frame
frame = simplegui.create_frame('OOP Memory', 2 * TILE_WIDTH, TILE_HEIGHT)
frame.set_draw_handler(draw)

# create tiles
tile1 = Tile(3, True, [0, TILE_HEIGHT])
tile2 = Tile(5, False, [TILE_WIDTH, TILE_HEIGHT])

###################################################
# Testing code



####################################################
# Output of testing code
