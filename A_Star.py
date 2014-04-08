# Project 3
# Joel Scott
# jascott@uga.edu

import pygame, sys
from pygame.locals import *

file = input('Please choose file:')
startX = input('Please enter the starting point x value:')
startY = input('Please enter the starting point y value:')
endX = input('Please enter the ending point x value:')
endY = input('Please enter the ending point y value:')
startX = int(startX)
startY = int(startY)
endX = int(endX)
endY = int(endY)

currentNodeHolder = []
gHold = 0
gFix = 0
done = [endX, endY]
openList = list()
closedList = list()
currentNode = []
node = [0, 0]
lowest = []
gridLength = 0
gridHeight = 0

mapFile = open(file + '.txt', 'r')
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
    global displayMap, openList, closedList, currentNode, gHold, gFix, currentNodeHolder
    pygame.init()
    displayMap = pygame.display.set_mode((windowWidth, windowHeight))
    pygame.display.set_caption('Project 3')
    for x in range(gridWidth):
        for y in range(gridHeight):
            if 'o' == spaces[x + y * gridWidth]:
            #add obstacle squares to closed list
                node = [x, y]
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
    #currentNode at x,       y
    currentNode = [startX, startY]
    openList.append(currentNode)
    gHold = 0
    while currentNode != done:
        if openList != []:
            openList.remove(currentNode)
            closedList.append(currentNode)
            parent = [currentNode[0], currentNode[1]]
            gHold = gFix + gHold
        for i in range(8):
            if i == 0 and currentNode[0] + 1 < gridWidth:
            #to right of parent
                possible = [currentNode[0] + 1, currentNode[1]]
                if possible in closedList or possible in openList:
                    continue
                else:
                    openList.append(possible)
            elif i == 1 and (currentNode[0] + 1 < gridWidth and currentNode[1] + 1 < gridHeight):
            #right/down
                possible = [currentNode[0] + 1, currentNode[1] + 1]
                if possible in closedList or possible in openList:
                    continue
                elif [currentNode[0] + 1, currentNode[1]] in closedList or [currentNode[0], currentNode[1] + 1] in closedList:
                    continue
                else:
                    openList.append(possible)
            elif i == 2 and currentNode[1] + 1 < gridHeight:
            #down
                possible = [currentNode[0], currentNode[1] + 1]
                if possible in closedList or possible in openList:
                    continue
                else:
                    openList.append(possible)
            elif i == 3 and (currentNode[0] - 1 >= 0 and currentNode[1] + 1 < gridHeight):
            #left/down
                possible = [abs(currentNode[0] - 1), currentNode[1] + 1]
                if possible in closedList or possible in openList:
                    continue
                elif [currentNode[0] - 1, currentNode[1]] in closedList or [currentNode[0], currentNode[1] + 1] in closedList:
                    continue
                else:
                    openList.append(possible)
            elif i == 4 and currentNode[0] - 1 >= 0:
            #left
                if currentNode[0] - 1 == 0:
                    possible = [currentNode[0] - 1, currentNode[1]]
                else:
                    possible = [abs(currentNode[0] - 1), currentNode[1]]
                if possible in closedList or possible in openList:
                    continue
                else:
                    openList.append(possible)                
            elif i == 5 and (currentNode[0] - 1 >= 0 and currentNode[1] - 1 >= 0):
            #left/up
                possible = [abs(currentNode[0] - 1), abs(currentNode[1] - 1)]
                if possible in closedList or possible in openList:
                    continue
                elif [currentNode[0] - 1, currentNode[1]] in closedList or [currentNode[0], currentNode[1] - 1] in closedList:
                    continue
                else:
                    openList.append(possible)
            elif i == 6 and currentNode[1] - 1 >= 0:
            #up
                possible = [currentNode[0], abs(currentNode[1] - 1)]
                if possible in closedList or possible in openList:
                    continue
                else:
                    openList.append(possible)
            elif i == 7 and (currentNode[1] - 1 >= 0 and currentNode[0] + 1 < gridWidth):
            #up/right
                possible = [currentNode[0] + 1, abs(currentNode[1] - 1)]
                if possible in closedList or possible in openList:
                    continue
                elif [currentNode[0] + 1, currentNode[1]] in closedList or [currentNode[0], currentNode[1] - 1] in closedList:
                    continue
                else:
                    openList.append(possible)
        for r in range(len(openList)):
            if (len(openList)) > 1:
                if r == 0:
                    compare1 = F(parent, openList[r])
                    continue
                else:
                    compare2 = F(parent, openList[r])
                    if compare1 > compare2:
                        lowest.append(compare2)
                        compare1 = compare2
                    elif compare2 > compare1:
                        lowest.append(compare1)
                        compare1 = compare2
                lowest.sort()
                if len(lowest) > 1:
                    if lowest[0] > lowest[1]:
                        lowest.remove(lowest[0])
                    elif lowest[1] > lowest[0]:
                        lowest.remove(lowest[1])
                    else:
                        lowest.remove(lowest[1])
        for x in range(len(openList)):
            if (len(openList)) > 1:
                if lowest[0] == F(parent, openList[x]):
                    currentNode = openList[x]
            else:
                currentNode = openList[x]
        G(parent, currentNode)
        currentNodeHolder.append(currentNode)
        print(currentNode)
        
def G(parent, openNode): #parent and openNode (x, y)
    X = sum(parent)
    Y = sum(openNode)
    value = abs(Y - X)
    if (value % 2) == 0:
        G = 14 + gHold
        gFix = 14
    else:
        G = 10 + gHold
        gFix = 10
    return G

def H(openNode): #openNode (x, y)
    c = [endX, endY]
    hx = abs(endX - openNode[0])
    hy = abs(endY - openNode[1])
    X = hx + hy
    H = X * 10
    return H

def F(parent, openNode):
    F = G(parent, openNode) + H(openNode)
    return F
    
def pixelCoord(x, y):
    return xMargin + x * tileSize + 1, yMargin + y * tileSize + 1
    
def drawGrid():
    displayMap.fill(backGround)
#    font = pygame.font.SysFont(None, 24)
#    text = font.render(str(len(currentNodeHolder)), 1, (255, 255, 0))
#    label = font.render("Steps = + text", 1, (255, 255, 0))
#    displayMap.blit(label, (100, 100))
                       
    
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
    for x in range(len(currentNodeHolder)):
        hold = currentNodeHolder[x]
        x = hold[0]
        y = hold[1]
        pixX, pixY = pixelCoord(x, y)
        pygame.draw.rect(displayMap, lineColor, (pixX + 7, pixY + 7, tileSize - 15, tileSize -15))
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
