# Project 3
# Joel Scott
# jascott@uga.edu

import pygame, sys
from pygame.locals import *

#grid = input('Please choose square, rectangle, or hexagon:')
#startX = input('Please enter the starting point x value:')
#startY = input('Please enter the starting point y value:')
#endX = input('Please enter the ending point x value:')
#endY = input('Please enter the ending point y value:')
gridLength = 0
gridHeight = 0

mapFile = open('map.txt', 'r')
spaces = []
for line in mapFile:
    gridHeight = gridHeight + 1
    for c in line:
        if c != '\n':
            spaces.append(c)

gridWidth = int(len(spaces)/gridHeight)
    
windowWidth = 50 * gridWidth + 200
windowHeight = 50 * gridHeight + 200
tileSize = 50

xMargin = int((windowWidth - (gridWidth * tileSize)) / 2)
yMargin = int((windowHeight - (gridHeight * tileSize)) /2)

fps = 30
startTileColor = (0, 255, 0)
endTileColor = (255, 0, 0)
lineColor = (0, 0, 255)
obsticaleColor = (255, 0, 255)
backGround = (0, 0, 0)

def main():

    global displayMap

    pygame.init()
    displayMap = pygame.display.set_mode((windowWidth, windowHeight))
    pygame.display.set_caption('Project 3')
    while True:
        drawArea()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
    
def drawArea():

    displayMap.fill(backGround)
    for x in range(gridWidth + 1):
        firstx = x * tileSize + xMargin
        firsty = yMargin
        lastx = x * tileSize + xMargin
        lasty = yMargin + gridHeight * tileSize
        pygame.draw.line(displayMap, lineColor, (firstx, firsty), (lastx, lasty))

    for y in range(gridHeight + 1):
        firstx = xMargin
        firsty = y * tileSize + yMargin
        lastx = xMargin + gridWidth * tileSize
        lasty = yMargin + y * tileSize
        pygame.draw.line(displayMap, lineColor, (firstx, firsty), (lastx, lasty))


if __name__ == '__main__':
    main()
