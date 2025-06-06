import pygame
import os
import praise

spaceHeld = False

def makeWind(x=0, y=0, image="ghost.png"):

    if type(x) == tuple and y == 0:
        print("you've tupled!")
        x, y = list(x)
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)

    w, h = 263, 187
    screen = pygame.display.set_mode((w, h))
    pygame.display.set_icon(pygame.image.load("icon.png"))

    # RENDER YOUR GAME HERE
    ghost = pygame.image.load(image).convert()
    screen.blit(ghost, (0, 0))
    pygame.display.set_caption("Ghost (spooky)(she/her)")

    # flip() the display to put your work on screen
    pygame.display.flip()

    pygame.time.wait(300)
    if pygame.key.get_pressed()[pygame.K_SPACE] and spaceHeld:
        praise.PraiseUser()
        pygame.quit()
    elif pygame.key.get_pressed()[pygame.K_SPACE] and not spaceHeld:
        spaceHeld = True
        pygame.quit()
    elif not pygame.key.get_pressed()[pygame.K_SPACE]:
        spaceHeld = False
        pygame.quit()
    else:
        print("I don't know what you're doing, but it's too magical for this humble program")