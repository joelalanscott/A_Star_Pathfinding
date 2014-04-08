# Project 3
# Joel Scott
# jascott@uga.edu

import pygame, sys
from pygame.locals import *

#grid = input('Please choose square, rectangle, or hexagon:')
startX = input('Please enter the starting point x value:')
startY = input('Please enter the starting point y value:')
endX = input('Please enter the ending point x value:')
endY = input('Please enter the ending point y value:')
startX = int(startX)
startY = int(startY)
endX = int(endX)
endY = int(endY)

openList = list()
closedList = list()

node = (0, 0, [0,0])

gridLength = 0
gridHeight = 0

mapFile = open('map.txt', 'r')
spaces = []
for line in mapFile:
    gridHeight = gridHeight + 1
    for gitHub in line:
        if gitHub != '\n':
            spaces.append(gitHub)

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
obstacleColor = (255, 0, 255)
backGround = (0, 0, 0)

def main():
    global displayMap, openList, closedList
    pygame.init()
    displayMap = pygame.display.set_mode((windowWidth, windowHeight))
    pygame.display.set_caption('Project 3')
    for x in range(gridWidth):
        for y in range(gridHeight):
            if 'o' == spaces[x + y * gridWidth]:
            #add obstacle squares to closed list
                node = (x, y, [-1, -1])
                closedList.append(node)
    startAStar()
    while True:
        drawGrid()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

def startAStar():
    parent = [startX, startY]
    #currentNode at x,       y,     parent
    currentNode = (startX, startY, [-1, -1])
    openList.append(currentNode)
#    while openList:
#        if currentNode :
            
            
def G(parent, openNode):
    X = sum(parent)
    Y = sum(openNode)
    value = abs(X - Y)
    if (value % 2) == 0:
        G = 14
    else:
        G = 10
#    openList.append(G)
    return G

def H(openNode):
    H = [endX, endY]
    H = sum(H)
    X = sum(openNode)
    H = (H - X) * 10
#    openList.append(H)
    return H
    
def pixelCoord(x, y):
    return xMargin + x * tileSize + 1, yMargin + y * tileSize + 1

def drawGrid():
    displayMap.fill(backGround)
    for x in range(gridHeight + 1):
    #draw horizontal lines
        firstx = xMargin
        firsty = x * tileSize + yMargin
        lastx = xMargin + gridWidth * tileSize
        lasty = yMargin + x * tileSize
        pygame.draw.line(displayMap, lineColor, (firstx, firsty), (lastx, lasty))
    for x in range(gridWidth + 1):
    #draw vertical lines
        firstx = x * tileSize + xMargin
        firsty = yMargin
        lastx = x * tileSize + xMargin
        lasty = yMargin + gridHeight * tileSize
        pygame.draw.line(displayMap, lineColor, (firstx, firsty), (lastx, lasty))
    for x in range(gridWidth):
        for y in range(gridHeight):
            rectx, recty = pixelCoord(x, y)
            if startX == x and startY == y:
            #draw start square
                newSX, newSY = pixelCoord(x, y)
                pygame.draw.rect(displayMap, startTileColor, (newSX, newSY, tileSize - 1, tileSize - 1))
            if endX == x and endY == y:
            #draw end square
                newEX, newEY = pixelCoord(x, y)
                pygame.draw.rect(displayMap, endTileColor, (newEX, newEY, tileSize - 1, tileSize - 1))
            if 'o' == spaces[x + y * gridWidth]:
            #draw obstacle squares
                pygame.draw.rect(displayMap, obstacleColor, (rectx, recty, tileSize - 1, tileSize - 1))

if __name__ == '__main__':
    main()
