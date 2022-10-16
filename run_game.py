from array import *
import os
from turtle import title
import pygame
from pygame.locals import *
import time

pygame.init()

# ----------------------  Player Related Variables  ---------------------- #
PLAYER_X = 7
PLAYER_Y = 10
CanMove = True

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
WIDTH = 20
HEIGHT = 20
MARGIN = 0

# Text Related
titleFont = pygame.font.Font("runescape_uf.ttf", 36)
textFont = pygame.font.Font("runescape_uf.ttf", 24)
currentTitle = "RATSCAPE"
currentText = "Welcome"
collisionText = "You can't go that way"

# ----------------------  Map Related  ---------------------- #
currentMap = "Dungeon.txt"

# Load Map and remove whitespaces
with open(currentMap, "r") as f:
    Dungeon = f.readlines()

Dungeon = [x.replace(" ", "") for x in Dungeon]
Dungeon = [x.strip('\n') for x in Dungeon]

# This sets the WIDTH and HEIGHT of of the map for rendering
# this also allows for the map to be changed without having to change the code
mapColumns = len(Dungeon[0])
mapRows = len(Dungeon)

pygame.display.set_caption(windowTitle)
pygame.key.set_repeat()

# Find P in the map
for i in range(len(Dungeon)):
    for j in range(len(Dungeon[i])):
        if Dungeon[i][j] == "P":
            PLAYER_X = j
            PLAYER_Y = i

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
                    PLAYER_Y -= 1
                    
                    # if north is a wall
                    if Dungeon[PLAYER_Y][PLAYER_X] == "W":
                        currentTitle = "RATSCAPE"
                        currentText = collisionText
                        PLAYER_Y += 1
                    Dungeon[PLAYER_Y] = Dungeon[PLAYER_Y][:PLAYER_X] + "P" + Dungeon[PLAYER_Y][PLAYER_X + 1:]
                    Dungeon[PLAYER_Y + 1] = Dungeon[PLAYER_Y + 1][:PLAYER_X] + " " + Dungeon[PLAYER_Y + 1][PLAYER_X + 1:]
                    
                if event.key == pygame.K_s:
                    PLAYER_Y += 1
                    
                    # if south is a wall
                    if Dungeon[PLAYER_Y][PLAYER_X] == "W":
                        currentText = collisionText
                        PLAYER_Y -= 1
                    Dungeon[PLAYER_Y] = Dungeon[PLAYER_Y][:PLAYER_X] + "P" + Dungeon[PLAYER_Y][PLAYER_X + 1:]
                    Dungeon[PLAYER_Y - 1] = Dungeon[PLAYER_Y - 1][:PLAYER_X] + " " + Dungeon[PLAYER_Y - 1][PLAYER_X + 1:]

                # Left and Right
                if event.key == pygame.K_a:
                    PLAYER_X -= 1
                    
                    # if west is a wall
                    if Dungeon[PLAYER_Y][PLAYER_X] == "W":
                        currentText = collisionText
                        PLAYER_X += 1
                    Dungeon[PLAYER_Y] = Dungeon[PLAYER_Y][:PLAYER_X] + "P" + Dungeon[PLAYER_Y][PLAYER_X + 1:]
                    Dungeon[PLAYER_Y] = Dungeon[PLAYER_Y][:PLAYER_X + 1] + " " + Dungeon[PLAYER_Y][PLAYER_X + 2:]

                if event.key == pygame.K_d:
                    PLAYER_X += 1
                    
                    # if east is a wall
                    # or out of array bounds
                    if Dungeon[PLAYER_Y][PLAYER_X] == "W":
                        currentText = collisionText
                        PLAYER_X -= 1
                    Dungeon[PLAYER_Y] = Dungeon[PLAYER_Y][:PLAYER_X] + "P" + Dungeon[PLAYER_Y][PLAYER_X + 1:]
                    Dungeon[PLAYER_Y] = Dungeon[PLAYER_Y][:PLAYER_X - 1] + " " + Dungeon[PLAYER_Y][PLAYER_X:]

            if event.key == pygame.K_q:
                CanMove = False
                currentText = "You are now unable to move."
            
            if event.key == pygame.K_e:
                CanMove = True
                currentText = "You are now able to move."

                
    
    for row in range(mapRows):
        for column in range(mapColumns):
            color = pygame.Color('chartreuse4')
            if Dungeon[row][column] == 'P':
                color = pygame.Color('blue')
            if Dungeon[row][column] == 'L':
                color = pygame.Color('green')
            if Dungeon[row][column] == 'D':
                color = pygame.Color('brown')
            if Dungeon[row][column] == 'W':
                color = pygame.Color('grey')
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

