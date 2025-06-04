import pygame
import os

def init():
    spaceHeld = False

def makeWind(x=0,y=0):

    if type(x) == tuple and y == 0:
        print("you've tupled!")
        x,y = list(x)
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

    w,h = 263,187
    screen = pygame.display.set_mode((w, h))
    pygame.display.set_icon(pygame.image.load("icon.png"))

    # RENDER YOUR GAME HERE
    ghost = pygame.image.load("ghost.png").convert()
    screen.blit(ghost, (0,0))
    pygame.display.set_caption("Ghost (spooky)")

    # flip() the display to put your work on screen
    pygame.display.flip()

    pygame.time.wait(300)
    if pygame.key.get_pressed()[pygame.K_SPACE] and spaceHeld:
        print("bye")
        return False
    elif pygame.key.get_pressed()[pygame.K_SPACE] and not spaceHeld:
        spaceHeld = True
        print("once")
    elif not pygame.key.get_pressed()[pygame.K_SPACE]:
        spaceHeld = False
        print("no")
    return True