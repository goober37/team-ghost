import pygame as pg
import praise

# pg setup
pg.init()
screen = pg.display.set_mode((300,300))
clock = pg.time.Clock()
pg.font.init()

for i in range(60):

    #clear screen
    screen.fill("black")

    # RENDER YOUR GAME HERE
    skeleton = pg.image.load("skelefinger.jpg").convert()
    screen.blit(skeleton, (0,0))

    if pg.font:
        font = pg.font.Font(None, 64)
        text = font.render("NO", True, (255, 255, 255))
        textpos = text.get_rect(centerx=150, y=150)
        screen.blit(text, textpos)

    # flip() the display to put your work on screen
    pg.display.flip()

    clock.tick(60)  # limits FPS to 60

pg.quit()