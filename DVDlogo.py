import pygame as pg

#set everything up
pg.init()
pg.font.init()
screen = pg.display.set_mode()
clock = pg.time.Clock()
boundx, boundy = pg.display.get_window_size()
running = True
textvel = [10,10]
debug = "no"

#math the font
font = pg.font.Font(None, 64)
text = font.render("DVD", True, (255, 255, 255))
textpos = text.get_rect(x=1, y=1)

def bounceInner(bound=pg.Rect(0,0,100,100), inner=pg.Rect(0,0,10,10),vel=[10,10], noise=0):
    pg.mixer.init()
    if inner[0] <= bound[0] or inner[0]+inner[2] >= bound[0]+bound[2]:
        if noise==0:
            0+0
        else:
            pg.mixer.music.load(noise)
            pg.mixer.music.play()
        vel[0] *= -1
        inner = inner.move(vel[0] , 0)
    if inner[1] <= bound[1] or inner[1] + inner[3] >= bound[1] + bound[3]:
        if noise==0:
            0+0
        else:
            pg.mixer.music.load(noise)
            pg.mixer.music.play()
        vel[1] *= -1
        inner = inner.move(0 , vel[1])
    return inner, vel

# while running:
#     # poll for events
#     # pygame.QUIT event means the user clicked X to close your window
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             running = False
#     #clear screen
#     screen.fill("black")

#     # RENDER YOUR GAME HERE
#     if pg.font:
#         #move font
#         textpos = textpos.move(textvel[0],textvel[1])
#         textpos, textvel = bounceInner([0,0,boundx,boundy],textpos, textvel)
#         #render font
#         screen.blit(text, textpos)
#     #draw debug stuff
#     if debug == "yes":
#         pg.draw.rect(screen,(255,0,0),textpos, width=3)
#         pg.draw.circle(screen,"green",(textpos[0],textpos[1]),3)
#     #cleanup
#     pg.display.flip()
#     clock.tick(30)
# pg.quit()