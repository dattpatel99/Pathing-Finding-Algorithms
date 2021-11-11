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

from tkinter import *
from tkinter import messagebox

from constants import *
from PathFinding import Graph, Queue

# Alert Message for User
ALERT_MESSAGE = None

# Initialize pygame
pygame.init()
FONT = pygame.font.SysFont('Corbel',30)

# Drag value
drag = False
setStart = False
setDestination = False 
grid = Graph(ROW, COL)
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("Pathfinding with Dijsktra's Algorithm")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

def run(graph: Graph):
    #qeue to hold list of nodes to check 
    nodes_check = Queue()
    source = graph.getSource()
    if source == None:
        return None, "No Source set"
    source.setVisited()
    destination = graph.getDestination()
    if destination == None:
        return None, "No Destination set"
    nodes_check.insert(source)
    reached = False

    # Dijkarta's Algo
    while nodes_check.length() != 0:
        cur_node = nodes_check.pop()
        neighbours = cur_node.findNeighbours(graph.getGraph())
        for each in neighbours:
            if each == destination:
                reached = True
                each.setPrev(cur_node)
                break
            each.setPrev(cur_node)
            each.setVisited()
            each.setDist(cur_node.getDist() + 1)
            nodes_check.insert(each)
        drawGrid()
        pygame.display.flip()
        clock.tick(60)
        if reached:
            break
    return reached, "Path Found"

def handleRunResult(grid: Graph, result):
    if result == True:
        grid.setPath
    else: 
        Tk().wm_withdraw()
        messagebox.showinfo("Alert Message", ALERT_MESSAGE)
        
def drawGrid():
    # Draw the grid
    for row in range(ROW):
        for column in range(COL):
            val = grid.getDist(row, column)
            type = grid.getType(row, column)
            inShort = grid.getInShort(row, column)
            if not inShort:
                if type == None and val == INFITY:
                    color = WHITE
                elif  type == "Wall":
                    color = BLACK
                elif type == "Destination":
                    color = RED
                elif type == "Source":
                    color = GREEN
                else:
                    color = BLUE
            else:
                color = MAIN_PATH
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

    # Clear Walls Program
    verPos += (BUTTON_VER + BUTTON_H)
    drawRect(screen, BUTTON_COLOR, horPos, verPos, BUTTON_W, BUTTON_H)
    
    text = FONT.render('Clear Walls' , True , TEXT_COLOR)
    screen.blit(text, (horPos,verPos+10))

    # For Reset Program
    verPos += (BUTTON_VER + BUTTON_H)
    drawRect(screen, BUTTON_COLOR, horPos, verPos, BUTTON_W, BUTTON_H)
    
    text = FONT.render('Reset Program' , True , TEXT_COLOR)
    screen.blit(text, (horPos,verPos+10))

def handleWalls(gridType, gridVal):
    if gridVal == -1 and gridType == "Wall":
        grid.setDist(row,column,wordToNumber["Open"])
        grid.setType(row, column, None)
    elif gridVal == INFITY and gridType == None:
        grid.setDist(row,column, wordToNumber[current])
        grid.setType(row, column, "Wall")

def handleDestination(gridType, gridVal):
    if gridType == "Destination" and grid.getDestination() != None:
        grid.resetDestination()
        grid.setDist(row,column, wordToNumber["Open"]) 
        grid.setType(row, column, None)                    
    elif gridVal == INFITY and grid.getDestination() == None:
        grid.setDestination(row, column)
        grid.setType(row, column, "Destination")

def handleStart(gridVal):
    if gridVal == 0 and grid.getSource() != None:
        grid.setDist(row,column, wordToNumber["Open"]) 
        grid.resetSource()
        grid.setType(row, column, None)
    elif gridVal == INFITY and grid.getSource() == None:
        grid.setDist(row,column, wordToNumber[current])
        grid.setSource(row, column)
        grid.setType(row, column, "Source")

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        # User clicks the mouse. Get the position
        pos = pygame.mouse.get_pos()

        # Change the x/y screen coordinates to grid coordinates
        column = int(pos[0] // (WIDTH + MARGIN))
        row = int(pos[1] // (HEIGHT + MARGIN))

        if event.type == pygame.QUIT:  # If user clicked close
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # If in grid
            if row <= int(ROW-1) and column <= int(COL-1):
                gridVal = grid.getDist(row,column)
                gridType = grid.getType(row, column)
                # Handles start button and grid events
                if current == "Start":
                    handleStart(gridVal)
                # Handles destination button and grid events
                elif current == "Destination":
                   handleDestination(gridType, gridVal)
                # Handles wall grid events
                elif current == "Wall":
                    drag = True
                    handleWalls(gridType, gridVal)
            # For buttons
            else:
                ver = (pos[1]) // (BUTTON_H + BUTTON_VER)
                if ver < 3:
                    current = buttonList[ver]
                else: 
                    if ver == 3:
                        grid.resetForReRun()
                        found, ALERT_MESSAGE = run(grid)
                        if found:
                            grid.setPath() 
                        elif found == False:
                            ALERT_MESSAGE = "No Path Found"
                        handleRunResult(grid, found)
                    elif ver == 4:
                        grid.clearWalls()
                    elif ver == 5:
                        grid.resetAll()
        elif event.type == pygame.MOUSEBUTTONUP:
            if current == "Wall":
                drag = False
        elif event.type == pygame.MOUSEMOTION:
            if drag and current == "Wall":
                if row <= int(ROW-1) and column <= int(COL-1):
                    gridVal = grid.getDist(row,column)
                    gridType = grid.getType(row, column)
                    handleWalls(gridType, gridVal)
            
    screen.fill(BACKGRUOND)
    drawGrid()
    drawButtons()
    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

pygame.display.quit()
pygame.quit()