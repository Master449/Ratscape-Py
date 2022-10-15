from array import *
import os
import pygame
from pygame.locals import *
import time

pygame.init()

# ----------------------  Player Related Variables  ---------------------- #
PLAYER_X = 7
PLAYER_Y = 10
CanMove = True

# ----------------------  Rendering Variables  ---------------------- #
pygame.display.set_caption("RATSCAPE")
screen = pygame.display.set_mode((1080, 720))
background = pygame.Color('black')
running = True
pygame.key.set_repeat()

# Black Rectangle
black = pygame.Surface((1080, 480))

textBox_X = 30
textBox_Y = 500
 
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20
 
# This sets the margin between each cell
MARGIN = 0

font = pygame.font.SysFont('Arial', 36)
currentText = "RATSCAPE"

# ----------------------  Map Related Variables  ---------------------- #
currentMap = "Dungeon.txt"

with open(currentMap, "r") as f:
    Dungeon = f.readlines()

Dungeon = [x.replace(" ", "") for x in Dungeon]
Dungeon = [x.strip('\n') for x in Dungeon]

# Find P in the map
for i in range(len(Dungeon)):
    for j in range(len(Dungeon[i])):
        if Dungeon[i][j] == "P":
            PLAYER_X = j
            PLAYER_Y = i


# ----------------------  Game Loop  ---------------------- #
while running:
    pygame.time.Clock().tick(60)
    img = font.render(currentText, True, (255, 255, 255))
    screen.blit(black, (textBox_X, textBox_Y))
    screen.blit(img, (textBox_X, textBox_Y))

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
                        currentText = "You slam your head into the wall"
                        PLAYER_Y += 1
                    Dungeon[PLAYER_Y] = Dungeon[PLAYER_Y][:PLAYER_X] + "P" + Dungeon[PLAYER_Y][PLAYER_X + 1:]
                    Dungeon[PLAYER_Y + 1] = Dungeon[PLAYER_Y + 1][:PLAYER_X] + " " + Dungeon[PLAYER_Y + 1][PLAYER_X + 1:]
                if event.key == pygame.K_s:
                    PLAYER_Y += 1
                    
                    # if south is a wall
                    if Dungeon[PLAYER_Y][PLAYER_X] == "W":
                        currentText = "You slam your head into the wall"
                        PLAYER_Y -= 1
                    Dungeon[PLAYER_Y] = Dungeon[PLAYER_Y][:PLAYER_X] + "P" + Dungeon[PLAYER_Y][PLAYER_X + 1:]
                    Dungeon[PLAYER_Y - 1] = Dungeon[PLAYER_Y - 1][:PLAYER_X] + " " + Dungeon[PLAYER_Y - 1][PLAYER_X + 1:]

                # Left and Right
                if event.key == pygame.K_a:
                    PLAYER_X -= 1
                    
                    # if west is a wall
                    if Dungeon[PLAYER_Y][PLAYER_X] == "W":
                        currentText = "You slam your head into the wall"
                        PLAYER_X += 1
                    Dungeon[PLAYER_Y] = Dungeon[PLAYER_Y][:PLAYER_X] + "P" + Dungeon[PLAYER_Y][PLAYER_X + 1:]
                    Dungeon[PLAYER_Y] = Dungeon[PLAYER_Y][:PLAYER_X + 1] + " " + Dungeon[PLAYER_Y][PLAYER_X + 2:]
                if event.key == pygame.K_d:
                    PLAYER_X += 1
                    
                    # if east is a wall
                    if Dungeon[PLAYER_Y][PLAYER_X] == "W":
                        currentText = "You slam your head into the wall"
                        PLAYER_X -= 1
                    Dungeon[PLAYER_Y] = Dungeon[PLAYER_Y][:PLAYER_X] + "P" + Dungeon[PLAYER_Y][PLAYER_X + 1:]
                    Dungeon[PLAYER_Y] = Dungeon[PLAYER_Y][:PLAYER_X - 1] + " " + Dungeon[PLAYER_Y][PLAYER_X:]

            if event.key == pygame.K_q:
                CanMove = False
                print("Player can't move")
            
            if event.key == pygame.K_e:
                CanMove = True
                print("Player can move")

                
    
    for row in range(24):
        for column in range(54):
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

