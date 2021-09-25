import pygame

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BACKGRUOND = (232, 203, 121)

# Text Related
TEXT_COLOR = BLACK
SELECTED_TEXT = WHITE


# Grid 
# Col and Row lengths
COL = 15
ROW = 15
# This sets the margin between each cell
MARGIN = 5
# Grid WIDTH and HEIGHT
WIDTH = 20
HEIGHT = 20

# Button Things
buttonList = ["Start", "Wall", "Destination"]
wordToNumber = {"Start": 0, "Wall": -1, "Destination": 9, "Run Dijsktra\'s": None, "Open": 1}
current = "Start"
# Button Dimensions
BUTTON_W = 200
BUTTON_H = 40
# Button margins
BUTTON_HOR = 10
BUTTON_VER = 5
# Button colors
BUTTON_COLOR = WHITE
SELECTED = (3, 244, 252)

#HEIGHT and WIDTH of the Screen
WINDOW_SIZE = [600, 500] 