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
ghop = pygame.Rect((bigx/2)-131, (bigy/2)-143, 263, 187) #ghost position as a rect
ghov = [30*np.random.randint(-1,1),30*np.random.randint(-1,1)] #ghost velocity as a list
#makes sure that ghov != 0
while ghov[0] == 0 or ghov[1] == 0:
    ghov = [30*np.random.randint(-1,1),30*np.random.randint(-1,1)]
while running:
    #move the ghost window
    ghop = pygame.Rect(ghop[0]+ghov[0],ghop[1]+ghov[1],ghop[2],ghop[3])
    ghop, ghov, bump = dvd.bounceInner(screenborders, ghop, ghov, True)
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