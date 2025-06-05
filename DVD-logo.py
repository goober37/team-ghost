import pygame as pg

pg.init()
pg.font.init()
screen = pg.display.set_mode()
clock = pg.time.Clock()
boundx, boundy = pg.display.get_window_size()
running = True
textposx = 0
textposy = 0
textvelx = 10
textvely = 10

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event == pg.K_ESCAPE:
                running == False
    #clear screen
    screen.fill("black")

    # RENDER YOUR GAME HERE
    if pg.font:
        font = pg.font.Font(None, 64)
        text = font.render("DVD", True, (255, 255, 255))
        textpos = text.get_rect(x=textposx, y=textposy)
        screen.blit(text, textpos)
        textposx += textvelx
        textposy += textvely
        if textposy >= boundy - textpos[3]:
            textvely *= -1
            textpos.move(0,textvely)
    
    #cleanup
    pg.display.flip()
    clock.tick(60)
pg.quit()