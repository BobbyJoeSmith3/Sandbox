# Define an empty Tile class


#################################################
# Student adds code where appropriate

# definition of empty Tile class (use pass in the body)
class Tile():

    # definition of initializer
    def __init__(self, num, exp):
        self.number = num
        self.exposed = exp

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

# create two objects, my_tile and your_tile
my_tile = Tile(3, True)

###################################################
# Testing code

print my_tile
my_tile.hide_tile()
print my_tile
my_tile.expose_tile()
print my_tile


####################################################
# Output of testing code

#The value of the tile is 3 and the tile is exposed.
#The value of the tile is 3 and the tile is NOT exposed.
#The value of the tile is 3 and the tile is exposed.
