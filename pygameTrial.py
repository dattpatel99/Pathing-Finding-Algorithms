"""
 Example program to show using an array to back a grid on-screen.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/mdTeqiWyFnc
"""
from utils import drawRect
import pygame
from constants import *
from PathFinding import run

# Initialize pygame
pygame.init()
FONT = pygame.font.SysFont('Corbel',30)

setStart = False
setDestination = False 
'''
Create a 2 dimensional array. A two dimensional
array is simply a list of lists.
Set grid value
'''
grid = []
for row in range(ROW):
    grid.append([])
    for column in range(COL):
        grid[row].append(1)  
 
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("Pathfinding with Dijsktra's Algorithm")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

def drawGrid():
    # Draw the grid
    for row in range(ROW):
        for column in range(COL):
            color = WHITE
            val = grid[row][column]
            if val == 0:
                color = GREEN
            elif val == -1:
                color = BLACK
            elif val == 9:
                color = RED
            drawRect(screen, color, (MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT)

def drawButtons():
    horPos = (MARGIN + WIDTH) * COL + MARGIN + BUTTON_HOR
    verPos = BUTTON_VER
 
    butColor = BUTTON_COLOR
    textColor = TEXT_COLOR
    
    for i in range(len(buttonList)):
        if buttonList[i] == current:
            butColor = SELECTED
            textColor = SELECTED_TEXT
        else:
            butColor = BUTTON_COLOR
            textColor = TEXT_COLOR

        drawRect(screen, butColor, horPos, verPos, BUTTON_W, BUTTON_H)
        text = FONT.render(buttonList[i] , True , textColor)
        screen.blit(text , (horPos,verPos + 10))
        if i != len(buttonList)-1:
            verPos += (BUTTON_VER + BUTTON_H)
    
    # For Running Algorithm
    verPos += (BUTTON_VER + BUTTON_H)
    drawRect(screen, BUTTON_COLOR, horPos, verPos, BUTTON_W, BUTTON_H)
    
    text = FONT.render('Run Dijsktra\'s' , True , TEXT_COLOR)
    screen.blit(text, (horPos,verPos+10))

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)

            # If in grid
            if row <= ROW-1 and column <= COL-1:
                gridVal = grid[row][column]
                
                # Handles start button and grid events
                if current == "Start":
                    if gridVal == 0 and setStart:
                        grid[row][column] = wordToNumber["Open"]
                        setStart = False
                    elif gridVal == 1 and not setStart:
                        grid[row][column] = wordToNumber[current]
                        setStart = True
                # Handles destination button and grid events
                elif current == "Destination":
                    if gridVal == 9 and setDestination:
                        grid[row][column] = wordToNumber["Open"]
                        setDestination = False
                    elif gridVal == 1 and not setDestination:
                        grid[row][column] = wordToNumber[current]
                        setDestination = True

                # Handles other button and grid events
                else:
                    if gridVal == wordToNumber[current]:
                        grid[row][column] = wordToNumber["Open"]
                    else:   
                        grid[row][column] = wordToNumber[current]
            # For buttons
            else:
                ver = (pos[1]) // (BUTTON_H + BUTTON_VER)
                if ver < 3:
                    current = buttonList[ver]
                elif ver == 3:
                    print("Runing Algo")
                    run(grid)
                elif ver == 4:
                    print("Reset")
            
    screen.fill(BACKGRUOND)
    drawGrid()
    drawButtons()
    # Limit to 60 frames per second
    clock.tick(60)
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

pygame.display.quit()
pygame.quit()
