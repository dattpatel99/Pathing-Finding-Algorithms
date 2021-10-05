import sys

INFITY = sys.maxsize
ROW_COMB = [0, 0, 1, -1]
COL_COMB = [1, -1, 0, 0]

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BACKGRUOND = (232, 203, 121)
BLUE = (3, 244, 252)
GREEN = (0, 105, 62, 1)
MAIN_PATH = (0, 255, 0)

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
wordToNumber = {"Start": 0, "Wall": -1, "Destination": INFITY, "Run Dijsktra\'s": None, "Open": INFITY}
current = "Start"
# Button Dimensions
BUTTON_W = 200
BUTTON_H = 40
# Button margins
BUTTON_HOR = 10
BUTTON_VER = 5
# Button colors
BUTTON_COLOR = WHITE
SELECTED = BLUE

#HEIGHT and WIDTH of the Screen
WINDOW_SIZE = [600, 500] 