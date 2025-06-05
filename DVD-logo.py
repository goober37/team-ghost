import pygame as pg

pg.init()
pg.font.init()
screen = pg.display.set_mode()
clock = pg.time.Clock()
boundx, boundy = pg.display.get_window_size()
running = True
textposx = 0
textposy = 0
textvel = [10,10]

def bounceInner(bound=pg.Rect(0,0,100,100), inner=pg.Rect(0,0,10,10),vel=[10,10]):
    if inner[0]<=bound[0] or inner[0]+inner[2] >= bound[2]:
        vel[0] *= -1
        inner = inner.move(vel[0],0)
        return vel
    if inner[1] <= bound[1] or inner[1] + inner[3] >= bound[3]:
        vel[1] *= -1
        inner = inner.move(0,vel[1])
        return vel

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    #clear screen
    screen.fill("black")

    # RENDER YOUR GAME HERE
    if pg.font:
        #render font
        font = pg.font.Font(None, 64)
        text = font.render("DVD", True, (255, 255, 255))
        textpos = text.get_rect(x=textposx, y=textposy)
        screen.blit(text, textpos)
        #move font
        textposx =  textvel[0]
        textposy += textvel[1]
        textvel = bounceInner([0,0,boundx,boundy],textpos,textvel)

    
    #cleanup
    pg.display.flip()
    clock.tick(60)
pg.quit()