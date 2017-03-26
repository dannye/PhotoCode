#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Copyright 2017 Tommy Lynch, Daniel Harding

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import pygame
import tkinter as tk
from tkinter import filedialog
import subprocess
import frodo
pygame.init()

black=(0, 0, 0)



def text_objects(string, size):
    default_font = pygame.font.get_default_font()
    font_renderer = pygame.font.Font(default_font,size)
    textSurface = font_renderer.render(string, True, black)
    return textSurface, textSurface.get_rect()

def text(string, size, color, Surface, display_w, display_h):
    TextSurface, TextRect = text_objects(string, size)
    TextRect.center = ((display_w), (display_h))
    Surface.blit(TextSurface, TextRect)
    pygame.display.update()

def button(title, x,y,w,h,ic,ac,size, Surface, action, extraArgs):
    pygame.display.update()
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(Surface, ac, (x, y, w, h))
        pygame.draw.rect(Surface, black, (x, y, w, h), 1)
        text(title, size, black, Surface, x+(w/2), y + (h/2))
        pygame.display.update()
        if click[0] == 1:
            action(*extraArgs)
            pygame.time.delay(100) 
            return False
    else:
        pygame.draw.rect(Surface, ic, (x, y, w, h))
        pygame.draw.rect(Surface, black, (x, y, w, h), 1)
        text(title, size, black, Surface, x+(w/2), y + (h/2))
        pygame.display.update() 
    return True

def button_noFparam(title, x,y,w,h,ic,ac,size, Surface, action):
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(Surface, ac, (x, y, w, h))
        pygame.draw.rect(Surface, black, (x, y, w, h), 1)
        text(title, size, black, Surface, x+(w/2), y + (h/2))
        pygame.display.update()
        if click[0] == 1:
            action()
            pygame.time.delay(100)
            return False
    else:
        pygame.draw.rect(Surface, ic, (x, y, w, h))
        pygame.draw.rect(Surface, black, (x, y, w, h), 1)
        text(title, size, black, Surface, x+(w/2), y + (h/2))
        pygame.display.update()
    return True

def text_box(content, x,y,w,h,c,size, Surface):
    pygame.draw.rect(Surface, c, (x, y, w, h))
    pygame.draw.rect(Surface, black, (x, y, w, h), 1)    
    text(content, size, black, Surface, x+(w/2), y + (h/2))
    pygame.display.update() 

def text_box_txt(string, size, color, Surface, x, y):
    TextSurface, TextRect = text_objects(string, size)
    TextRect.left = x
    TextRect.top = y
    Surface.blit(TextSurface, TextRect)
    pygame.display.update()

def text_box_left(content, x,y,w,h,c,size, Surface):
    pygame.draw.rect(Surface, c, (x, y, w, h))
    #pygame.draw.rect(Surface, black, (x, y, w, h), 1)    
    text_box_txt(content, size, black, Surface, x, y)
    pygame.display.update() 
        
def loop_exit(flag, condition):
    flag = condition
    print (flag)
    return flag
    
def pygame_pass():
    pass

def easter_egg():
    pass

def scan():
    root = tk.Tk()
    root.withdraw()
    root.update()
    file_path = filedialog.askopenfilename()
    return_code = subprocess.call("Frodo.exe " + file_path, shell=True)
    if return_code == 0:
        return True
    return False

def load():
    frodo.parseFrodo("script.frodo")

def close():
    pygame.display.quit()
    pygame.quit()

