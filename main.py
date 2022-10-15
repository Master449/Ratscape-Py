from array import *
import os
import pygame
from pygame.locals import *
import time

pygame.init()

# Screen and Game Related Variables
pygame.display.set_caption("RATSCAPE")
screen = pygame.display.set_mode((1070, 720))
background = pygame.Color('grey')
running = True
pygame.key.set_repeat()

# Player Related Variables
PLAYER_X = 7
PLAYER_Y = 10
CanMove = True

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
RED = (255, 0, 0)
GRAY = (128, 128, 128)
BROWN = (165, 42, 42)
 
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 25
HEIGHT = 25
 
# This sets the margin between each cell
MARGIN = 3

# Map Related Variables
currentMap = "Dungeon.txt"

with open(currentMap, "r") as f:
    Dungeon = f.readlines()

Dungeon = [x.replace(" ", "") for x in Dungeon]
Dungeon = [x.strip('\n') for x in Dungeon]

print(Dungeon)

while running:
    #print("Player X: " + str(PLAYER_X) + " Player Y: " + str(PLAYER_Y))

    # Apply background
    #screen.fill(background)

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
                    print("Player moved up")
                    Dungeon[PLAYER_Y] = Dungeon[PLAYER_Y][:PLAYER_X] + "P" + Dungeon[PLAYER_Y][PLAYER_X + 1:]
                    Dungeon[PLAYER_Y + 1] = Dungeon[PLAYER_Y + 1][:PLAYER_X] + " " + Dungeon[PLAYER_Y + 1][PLAYER_X + 1:]
                if event.key == pygame.K_s:
                    PLAYER_Y += 1
                    print("Player moved down")
                    Dungeon[PLAYER_Y] = Dungeon[PLAYER_Y][:PLAYER_X] + "P" + Dungeon[PLAYER_Y][PLAYER_X + 1:]
                    Dungeon[PLAYER_Y - 1] = Dungeon[PLAYER_Y - 1][:PLAYER_X] + " " + Dungeon[PLAYER_Y - 1][PLAYER_X + 1:]

                # Left and Right
                if event.key == pygame.K_a:
                    PLAYER_X -= 1
                    print("Player moved left")
                    Dungeon[PLAYER_Y] = Dungeon[PLAYER_Y][:PLAYER_X] + "P" + Dungeon[PLAYER_Y][PLAYER_X + 1:]
                    Dungeon[PLAYER_Y] = Dungeon[PLAYER_Y][:PLAYER_X + 1] + " " + Dungeon[PLAYER_Y][PLAYER_X + 2:]
                if event.key == pygame.K_d:
                    PLAYER_X += 1
                    print("Player moved right")
                    Dungeon[PLAYER_Y] = Dungeon[PLAYER_Y][:PLAYER_X] + "P" + Dungeon[PLAYER_Y][PLAYER_X + 1:]
                    Dungeon[PLAYER_Y] = Dungeon[PLAYER_Y][:PLAYER_X - 1] + " " + Dungeon[PLAYER_Y][PLAYER_X:]

            if event.key == pygame.K_q:
                CanMove = False
                print("Player can't move")
            
            if event.key == pygame.K_e:
                CanMove = True
                print("Player can move")

                
    
    for row in range(16):
        for column in range(38):
            color = WHITE
            if Dungeon[row][column] == 'P':
                color = BLUE
            if Dungeon[row][column] == 'L':
                color = GREEN
            if Dungeon[row][column] == 'D':
                color = BROWN
            if Dungeon[row][column] == 'W':
                color = GRAY
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

