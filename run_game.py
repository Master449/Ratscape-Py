from array import *
import os
from turtle import title
import pygame
from pygame.locals import *
import time

pygame.init()

# ----------------------  Player Related Variables  ---------------------- #
playerX = 7
playerY = 10
CanMove = True

theRat = pygame.image.load("rat.png")
ratRect = theRat.get_rect()

# ----------------------  Rendering / Font Variables  ---------------------- #
windowTitle = "RATSCAPE"
screen = pygame.display.set_mode((1080, 720))
background = pygame.Color('black')
running = True

# Black Rectangle
textEraser = pygame.Surface((1080, 480))
textBox_X = 30
textBox_Y = 500
 
# Map Cells
cellWidth = 20
cellHeight = 20
cellMargin = 0

# Text Related
titleFont = pygame.font.Font("runescape_uf.ttf", 36)
textFont = pygame.font.Font("runescape_uf.ttf", 24)
currentTitle = "RATSCAPE"
currentText = "Welcome"
collisionText = "You can't go that way"

# ----------------------  Map Related  ---------------------- #
currentMap = "Dungeon.txt"
grassColor = 'chartreuse4'
playerColor = 'blue'
wallColor = 'gray'
doorColor = 'brown'
lootColor = 'gold'
enemyColor = 'red'

# Load Map and remove whitespaces
with open(currentMap, "r") as f:
    Dungeon = f.readlines()

Dungeon = [x.replace(" ", "") for x in Dungeon]
Dungeon = [x.strip('\n') for x in Dungeon]

# This sets the cellWidth and cellHeight of of the map for rendering
# this also allows for the map to be changed without having to change the code
mapColumns = len(Dungeon[0])
mapRows = len(Dungeon)

pygame.display.set_caption(windowTitle)
pygame.key.set_repeat()

# Find P in the map
for i in range(len(Dungeon)):
    for j in range(len(Dungeon[i])):
        if Dungeon[i][j] == "P":
            playerX = j
            playerY = i

# ----------------------  Game Loop  ---------------------- #
while running:
    pygame.time.Clock().tick(60)

    titleText = titleFont.render(currentTitle, True, (255, 255, 255))
    bodyText = textFont.render(currentText, True, (255, 255, 255))
    chadUnderline = textFont.render("_________________________________________________________________________", True, (255, 255, 255))

    screen.blit(textEraser, (textBox_X, textBox_Y))
    screen.blit(chadUnderline, (textBox_X, textBox_Y + 20))
    screen.blit(titleText, (textBox_X, textBox_Y))
    screen.blit(bodyText, (textBox_X, textBox_Y + 50))

    # Refresh the screen
    
    pygame.display.flip()

    # Check for player input
    for event in pygame.event.get():

        # Check if the player quits
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("GAME CLOSED")

        # Check if the player presses a key
        if event.type == pygame.KEYUP:
            if CanMove == True:
            # Up and Down
                if event.key == pygame.K_w:
                    playerY -= 1
                    
                    # if north is a wall
                    if Dungeon[playerY][playerX] == "W":
                        currentTitle = "RATSCAPE"
                        currentText = collisionText
                        playerY += 1
                    Dungeon[playerY] = Dungeon[playerY][:playerX] + "P" + Dungeon[playerY][playerX + 1:]
                    Dungeon[playerY + 1] = Dungeon[playerY + 1][:playerX] + " " + Dungeon[playerY + 1][playerX + 1:]
                    
                if event.key == pygame.K_s:
                    playerY += 1
                    
                    # if south is a wall
                    if Dungeon[playerY][playerX] == "W":
                        currentText = collisionText
                        playerY -= 1
                    Dungeon[playerY] = Dungeon[playerY][:playerX] + "P" + Dungeon[playerY][playerX + 1:]
                    Dungeon[playerY - 1] = Dungeon[playerY - 1][:playerX] + " " + Dungeon[playerY - 1][playerX + 1:]

                # Left and Right
                if event.key == pygame.K_a:
                    playerX -= 1
                    
                    # if west is a wall
                    if Dungeon[playerY][playerX] == "W":
                        currentText = collisionText
                        playerX += 1
                    Dungeon[playerY] = Dungeon[playerY][:playerX] + "P" + Dungeon[playerY][playerX + 1:]
                    Dungeon[playerY] = Dungeon[playerY][:playerX + 1] + " " + Dungeon[playerY][playerX + 2:]

                if event.key == pygame.K_d:
                    playerX += 1
                    
                    # if east is a wall
                    # or out of array bounds
                    if Dungeon[playerY][playerX] == "W":
                        currentText = collisionText
                        playerX -= 1
                    Dungeon[playerY] = Dungeon[playerY][:playerX] + "P" + Dungeon[playerY][playerX + 1:]
                    Dungeon[playerY] = Dungeon[playerY][:playerX - 1] + " " + Dungeon[playerY][playerX:]

            if event.key == pygame.K_q:
                CanMove = False
                currentText = "You are now unable to move."
            
            if event.key == pygame.K_e:
                CanMove = True
                currentText = "You are now able to move."
                
    for row in range(mapRows):
        for column in range(mapColumns):
            color = pygame.Color(grassColor)
            if Dungeon[row][column] == 'P':
                #color = pygame.Color(playerColor)
                pygame.sprite.Sprite(theRat)
            if Dungeon[row][column] == 'L':
                color = pygame.Color(lootColor)
            if Dungeon[row][column] == 'D':
                color = pygame.Color(doorColor)
            if Dungeon[row][column] == 'W':
                color = pygame.Color(wallColor)
            if Dungeon[row][column] == 'E':
                color = pygame.Color(enemyColor)
            pygame.draw.rect(screen,
                             color,
                             [(cellMargin + cellWidth) * column + cellMargin,
                              (cellMargin + cellHeight) * row + cellMargin,
                              cellWidth,
                              cellHeight])

