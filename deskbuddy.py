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
ghop = pygame.rect(bigx/2,bigy/2,263,187)
ghov = [5,5]

if not pygame.mixer.get_init():
    pygame.mixer.init()
pygame.mixer.music.load("spooktune.mp3")
pygame.mixer.music.play(-1) 

while running:
    rendghost.makeWind(ghop[0], ghop[1])
    ghop, ghov = dvd.bounceInner([pygame.rect(0,0,bigx,bigy)], ghop, ghov)
    with open("running.txt", "r", encoding="utf-8") as f:
        running = f
    
    clock.tick(30)  # limits FPS to 30

pygame.quit()