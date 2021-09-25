import pygame
def drawRect(screen, color, startPosHor, startPosVer, horizontalWidth, verticalHeight):
    pygame.draw.rect(screen, color, [startPosHor, startPosVer, horizontalWidth, verticalHeight])