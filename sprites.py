#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 17:48:36 2017

@author: tommy
"""

#https://gallery.technet.microsoft.com/Turtle-PNG-Bitmap-for-582b449c#content

import pygame
pygame.init()

white = (255, 255, 255)

tileSize = 50
MAX_WIDTH = 10
MAX_HEIGHT = 10

RIGHT = 0
DOWN  = 1
LEFT  = 2
UP    = 3

def rot_center(image, angle):
    rot_image = pygame.transform.rotate(image, angle)
    return rot_image
  
class turtle(pygame.sprite.Sprite):
    name = "Turtle.png"
    
    def __init__(self, startX, startY):
        pygame.sprite.Sprite.__init__(self)
        self.orientation = RIGHT
        self.gridX = startX
        self.gridY = startY
        #turtle.image.topleft(0, 250)
        self.image = pygame.image.load(self.name)
        self.rect = self.image.get_rect()
        self.rect.x = self.gridX * tileSize
        self.rect.y = self.gridY * tileSize
    
    def draw(self, surface):
        surface.blit(self.image,(self.rect.x, self.rect.y))
        pygame.display.update()
    
    def move_forward(self):
        success = False
        if self.orientation == RIGHT:
            if self.gridX < MAX_WIDTH - 1:
                self.gridX += 1
                success = True
        elif self.orientation == UP:
            if self.gridY > 0:
                self.gridY -= 1
                success = True
        elif self.orientation == LEFT:
            if self.gridX > 0:
                self.gridX -= 1
                success = True
        elif self.orientation == DOWN:
            if self.gridY < MAX_HEIGHT - 1:
                self.gridY += 1
                success = True
        
        self.rect.x = self.gridX * tileSize
        self.rect.y = self.gridY * tileSize
        
        return success
        
    
    def rotate_CW(self):
        self.image = rot_center(self.image, -90)
        self.orientation = (self.orientation + 1) % 4
            
    def rotate_CCW(self):
        self.image = rot_center(self.image, 90)
        self.orientation = (self.orientation + 3) % 4

"""
Turtle = turtle()
Turtle.draw(screen)

running = 1
while running <=5:
    Turtle.move_forward(orientation, screen)
    pygame.draw.rect(screen, white, (x, y, 50, 50))
    Turtle.rotate_CCW(orientation)
    pygame.draw.rect(screen, white, (x, y, 50, 50))
    Turtle.draw(screen)
    pygame.time.delay(1000)
    running +=1
"""
