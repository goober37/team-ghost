import pygame
import os

spaceHeld = False

def makeWind(x=0, y=0):

    if type(x) == tuple and y == 0:
        print("you've tupled!")
        x, y = list(x)
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)

    w, h = 263, 187
    screen = pygame.display.set_mode((w, h))
    pygame.display.set_icon(pygame.image.load("icon.png"))

    # RENDER YOUR GAME HERE
    ghost = pygame.image.load("ghost.png").convert()
    screen.blit(ghost, (0, 0))
    pygame.display.set_caption("Ghost (spooky)")

    # flip() the display to put your work on screen
    pygame.display.flip()

    pygame.event.pump()  # Make sure key states are updated

    pygame.time.wait(300)
    if pygame.key.get_pressed()[pygame.K_SPACE] and spaceHeld:
        print("bye")
        with open("running.txt", "w", encoding="utf-8") as f:
            f = False
        pygame.quit()
    elif pygame.key.get_pressed()[pygame.K_SPACE] and not spaceHeld:
        spaceHeld = True
        print("once")
        with open("running.txt", "w", encoding="utf-8") as f:
            f = True
        pygame.quit()
    elif not pygame.key.get_pressed()[pygame.K_SPACE]:
        spaceHeld = False
        print("no")
        with open("running.txt", "w", encoding="utf-8") as f:
            f = True
        pygame.quit()
    else:
        print("I don't know what you're doing, but it's too magical for this humble program")