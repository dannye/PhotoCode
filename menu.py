#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 03:10:32 2017

@author: tommy
"""

import pygame
import functions_main
import sprites
import script

pygame.init()

tileSize = 50
MAX_WIDTH = 10
MAX_HEIGHT = 10

RIGHT = 0
DOWN  = 1
LEFT  = 2
UP    = 3

grey= (169,169,169)
black = (0, 0, 0)
white = (255, 255, 255)
red = (210, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 190)
purple = (204, 0, 255)
cyan = (0, 200, 200)
yellow = (225, 225, 0)

bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
bright_blue = (0, 0, 255)
bright_purple = (255, 0, 255)
bright_cyan = (0, 255, 255)
bright_yellow = (255, 255, 0)

startNum = 0
wallNum= 1
endNum= 2
clearNum= 3

matches = {
           startNum:bright_green,
           wallNum:grey,
           endNum:bright_red,
           clearNum:white
           
           }

maze1 = [
         [1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1],
         [0,3,3,3,3,3,3,3,3,2],
         [1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1]
         
         ]            
        
maze2 = [
         [1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,2],
         [1,1,1,1,1,1,1,1,1,3],
         [1,1,1,1,1,1,1,1,1,3],
         [0,3,3,3,3,3,3,3,3,3],
         [1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1]
         
         ]  
               
maze3 = [
         [1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1],
         [0,3,3,3,1,1,3,3,3,2],
         [1,1,1,3,3,3,3,1,1,1],
         [1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1]
         
         ]

maze4 = [
         [1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1],
         [3,3,3,3,3,1,1,1,1,1],
         [3,1,1,1,3,1,1,1,1,1],
         [0,1,1,1,3,1,1,1,1,1],
         [1,1,1,1,3,1,1,1,1,1],
         [1,1,1,1,3,3,3,3,3,2],
         [1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1]
         
         ]
maze5 = [
         [1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1],
         [1,1,1,3,3,3,3,1,1,1],
         [1,1,1,3,1,1,3,1,1,1],
         [0,3,3,3,1,1,3,3,3,2],
         [1,1,1,3,1,1,3,1,1,1],
         [1,1,1,3,1,1,3,1,1,1],
         [1,1,1,3,3,3,3,1,1,1],
         [1,1,1,1,1,1,1,1,1,1]
         
         ]
maze6 = [
         [1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,3,1,3,1,1,1],
         [0,3,3,3,3,3,3,1,1,1],
         [1,1,1,1,1,1,3,3,3,2],
         [1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1]
         
         ]
maze7 = [
         [1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,3,3,3,2],
         [1,1,1,1,1,1,3,1,1,1],
         [1,1,1,1,1,1,3,1,1,1],
         [0,1,1,1,1,1,3,1,1,1],
         [3,3,3,1,1,1,3,1,1,1],
         [1,1,3,3,3,3,3,1,1,1],
         [1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1]
         
         ]
maze8 = [
         [1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1],
         [1,3,3,3,3,3,1,1,1,1],
         [1,2,1,1,1,3,1,1,1,1],
         [1,1,1,1,1,3,1,1,1,1],
         [0,3,3,3,3,3,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1]
         
         ]
maze9 = [
         [1,1,1,1,1,3,3,2,1,1],
         [1,1,1,1,3,3,1,1,1,1],
         [1,1,1,3,3,1,1,1,1,1],
         [1,1,3,3,1,1,1,1,1,1],
         [1,3,3,1,1,1,1,1,1,1],
         [0,3,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1]
         
         ]
maze10 = [
         [3,3,3,3,3,3,3,3,3,3],
         [3,1,1,1,1,1,1,1,1,3],
         [3,1,1,1,3,3,3,3,1,3],
         [3,3,1,1,3,1,1,3,1,3],
         [1,3,3,1,2,1,1,3,1,3],
         [0,1,3,1,1,1,1,3,1,3],
         [3,1,3,1,1,1,1,3,1,3],
         [3,1,3,3,3,3,3,3,1,3],
         [3,1,1,1,1,1,1,1,1,3],
         [3,3,3,3,3,3,3,3,3,3]
         
         ]

mazes = [maze1, maze2, maze3, maze4, maze5, maze6, maze7, maze8, maze9,maze10]

def Build(maze, xtra):
    startX = 0
    startY = 0
    endX = 0
    endY = 0
    current_maze = []
    
    current_maze = mazes[maze - 1]

    mapHeight = len(current_maze)
    mapWidth = len(current_maze[0])
    
    maxWidth = mapWidth * tileSize
    
    displayMaze= pygame.display.set_mode((mapWidth*tileSize + 200,mapHeight*tileSize))
    displayMaze.fill((white))
    pygame.display.set_caption("Photo Code: Maze")        
    
    for row in range(mapHeight):
        for column in range(mapWidth):
            pygame.draw.rect(displayMaze,matches[current_maze[row][column]],
                             (column*tileSize,row*tileSize,tileSize,tileSize))
            pygame.draw.rect(displayMaze,black,(column*tileSize,row*tileSize,tileSize,tileSize),1)
            if current_maze[row][column] == endNum:
                endX = column
                endY = row
            if current_maze[row][column] == startNum:
                startX = column
                startY = row
    pygame.display.update()
    
    running = True
    t = sprites.turtle(startX, startY)
    t.draw(displayMaze)
    
    while running:
        running = functions_main.button_noFparam("Back to main menu", maxWidth + 5, 200, 190, 40, red, bright_red, 20, displayMaze, functions_main.pygame_pass)
        """
        pygame.time.delay(500)
        pygame.draw.rect(displayMaze,matches[current_maze[t.gridY][t.gridX]],
                             (t.gridX*tileSize,t.gridY*tileSize,tileSize,tileSize))
        pygame.draw.rect(displayMaze,black,(t.gridX*tileSize,t.gridY*tileSize,tileSize,tileSize),1)
        o = t.orientation
        if o == RIGHT and t.gridX < MAX_WIDTH - 1:
            space = current_maze[t.gridY][t.gridX + 1]
        if o == DOWN and t.gridY < MAX_HEIGHT - 1:
            space = current_maze[t.gridY + 1][t.gridX]
        if o == LEFT and t.gridX > 0:
            space = current_maze[t.gridY][t.gridX - 1]
        if o == UP and t.gridY > 0:
            space = current_maze[t.gridY - 1][t.gridX]
        if space != wallNum:
            if not t.move_forward():
                t.rotate_CW()
        else:
            t.rotate_CW()
        t.draw(displayMaze)
        if t.gridX == endX and t.gridY == endY:
            running = False
        """
        
    screen = pygame.display.set_mode((800, 500))
    screen.fill((white))

maze_selector = [1,0]
current_maze_number = maze_selector[0]

def next_maze():
    current_maze_number = maze_selector[0]
    if (current_maze_number < 10):
        current_maze_number = current_maze_number + 1
    maze_selector[0] = current_maze_number
    print (current_maze_number)
    
def past_maze():  
    current_maze_number = maze_selector[0]
    if (current_maze_number > 1):
        current_maze_number = current_maze_number - 1
    maze_selector[0] = current_maze_number
    print (current_maze_number)
        
    
screen = pygame.display.set_mode((800, 500))
screen.fill((white))
pygame.display.set_caption("Photo Code: Main Menu")
pygame.display.update()

menu_loop =True

while menu_loop:
    pygame.draw.line(screen, black, (500, 0), (500, 500), 1)
    #no functionality in buttons
    functions_main.button_noFparam("MENU OPTIONS", 550, 25, 200, 50, bright_blue, bright_blue, 22, screen, functions_main.easter_egg)
    functions_main.button_noFparam("SCAN", 575, 120, 150, 40, red, bright_red, 18, screen, functions_main.scan)
    functions_main.button_noFparam("RUN", 575, 180, 150, 40, green, bright_green, 18, screen, functions_main.run)
    functions_main.button_noFparam("LOAD", 575, 240, 150, 40, purple, bright_purple, 18, screen, functions_main.load)
    functions_main.button_noFparam("EXIT", 575, 300, 150, 40, yellow, bright_yellow, 18, screen, functions_main.close)
    functions_main.button("PREVIEW MAZE", 575, 360, 150, 40, cyan, bright_cyan, 18, screen, Build, maze_selector)
    functions_main.button_noFparam("NEXT MAZE", 675, 425, 95, 35, cyan, bright_cyan, 15, screen, next_maze)
    functions_main.button_noFparam("PAST MAZE", 525, 425, 95, 35, cyan, bright_cyan, 15, screen, past_maze)
    #functions_main.text_box(current_maze_number, 627, 425, 35, 35, cyan, 15, screen)
    
    #instructions display
    functions_main.text_box("Welcome to Photo Code", 0, 0, 500, 75, bright_cyan, 30, screen)
    functions_main.text_box("Instructions",100, 100, 300, 50, bright_blue, 20, screen)
    functions_main.text_box_left("SCAN: Upload a code sheet", 25, 200, 450, 20, white, 18, screen)
    functions_main.text_box_left("RUN: Start the loaded program", 25, 235, 450, 20, white, 18, screen)
    functions_main.text_box_left("LOAD: Select a previous code to run", 25, 270, 450, 20, white, 18, screen)
    functions_main.text_box_left("EXIT: Close Photo Code", 25, 305, 450, 20, white, 18, screen)
    functions_main.text_box_left("PREVIEW MAZE: Display the current code", 25, 340, 450, 20, white, 18, screen)
    functions_main.text_box_left("NEXT MAZE: Go to a more difficult maze", 25, 375, 450, 20, white, 18, screen)
    functions_main.text_box_left("LAST MAZE: Go to a less difficult maze", 25, 410, 450, 20, white, 18, screen)