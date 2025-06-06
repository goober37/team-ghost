#import tkinter as tk
#from tkinter import messagebox
import pygame
import os
import rendghost
import numpy as np
import DVDlogo as dvd


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1,1))
clock = pygame.time.Clock()
running = True
bigx,bigy = pygame.display.get_desktop_sizes()[0]
screenborders = pygame.Rect(0,0,bigx,bigy) #screen as a rect
ghop = pygame.Rect((2*bigx/3), (2*bigy/3), 263, 187) #ghost position as a rect
ghov = [30,30] #ghost velocity as a rect

while running:
    #move the ghost window
    ghop = pygame.Rect(ghop[0]+ghov[0],ghop[1]+ghov[1],ghop[2],ghop[3])
    ghop, ghov, bump, state = dvd.bounceInner(screenborders, ghop, ghov)
    print(state)
    #make the ghost window (he might be hurt)
    if bump:
        rendghost.makeWind(ghop[0], ghop[1],"ghosthurt.png")
        pygame.mixer.init()
        pygame.mixer.music.load("spooktune.mp3")
        pygame.mixer.music.play(-1)
        print("owchies!")
    else:
        rendghost.makeWind(ghop[0], ghop[1])
    clock.tick(30)  # limits FPS to 30

pygame.quit()