import pygame as pg

#set everything up
pg.init()
pg.font.init()
screen = pg.display.set_mode()
clock = pg.time.Clock()
boundx, boundy = pg.display.get_window_size()
running = True
textvelx, textvely = 10,10

#math the font
font = pg.font.Font(None, 64)
text = font.render("DVD", True, (255, 255, 255))
textpos = text.get_rect(x=1, y=1)

def bounceInner(bound=pg.Rect(0,0,100,100), inner=pg.Rect(0,0,10,10),velx=0,vely=0):
    if inner[0] <= bound[0] or inner[0]+inner[2] >= bound[0]+bound[2]:
        velx *= -1
        inner = inner.move(velx , 0)
    if inner[1] <= bound[1] or inner[1] + inner[3] >= bound[1] + bound[3]:
        vely *= -1
        inner = inner.move(0 , vely)
    return velx, vely, inner

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
        #move font
        textpos.move(textvelx,textvely)
        textvelx, textvely, textpos = bounceInner([0,0,boundx,boundy],textpos, textvelx, textvely)
        #render font
        screen.blit(text, textpos)
    #draw debug stuff
    pg.draw.rect(screen,(255,0,0),textpos, width=3)
    pg.draw.circle(screen,"green",(textpos[0],textpos[1]),3)
    #cleanup
    pg.display.flip()
    clock.tick(2)
pg.quit()