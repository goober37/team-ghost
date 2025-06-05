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
print(bigx, bigy)
screenborders = pygame.Rect(0,0,bigx,bigy)
ghop = pygame.Rect(bigx/2,bigy/2,263,187)
ghov = [20,20]

if not pygame.mixer.get_init():
    pygame.mixer.init()
pygame.mixer.music.load("spooktune.mp3")
pygame.mixer.music.play(-1) 

while running:
    #move the ghost window
    ghop, ghov = dvd.bounceInner(screenborders, ghop, ghov)
    #make the ghost window
    rendghost.makeWind(ghop[0], ghop[1])

    with open("running.txt", "r", encoding="utf-8") as f:
        running = f
    
    clock.tick(30)  # limits FPS to 30

pygame.quit()