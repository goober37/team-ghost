#import tkinter as tk
#from tkinter import messagebox
import pygame
import praise
import os
import rendghost
import numpy as np

#test

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1,1))
clock = pygame.time.Clock()
running = True
bigx,bigy = pygame.display.get_desktop_sizes()[0]
ghox, ghoy = bigx/2,bigy/2

# --- MUSIC SETUP: Only run this ONCE before the loop ---
if not pygame.mixer.get_init():
    pygame.mixer.init()
pygame.mixer.music.load("spooktune.mp3")
pygame.mixer.music.play(-1) 
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         running = False

    running = rendghost.makeWind(ghox, ghoy)

    ghox = ghox + np.random.randint(-30,30)
    ghoy = ghoy + np.random.randint(-30,30)

    clock.tick(30)  # limits FPS to 30

pygame.quit()