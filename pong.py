import pygame, sys
from pygame import *
init()
fenetre=display.set_mode((494,353),RESIZABLE)
fond=image.load("fond.jpg").convert()
balle=image.load("balle.jpg").convert_alpha()
fenetre.blit(fond,(0,0))
display.flip()
for x in range(balle.get_size()[0]):
    for y in range(balle.get_size()[1]):
        couleur=balle.get_at((x,y))
        if couleur[0]+couleur[1]+couleur[2]>700:
            couleur[3]=0
            balle.set_at((x,y),couleur)

continuer=1

fond=image.load("fond.jpg").convert()
raquette=image.load("raquette.jpg").convert_alpha()
fenetre.blit(fond,(0,0))
display.flip()
for x in range(raquette.get_size()[0]):
    for y in range(raquette.get_size()[1]):
        couleur=raquette.get_at((x,y))
        if couleur[0]+couleur[1]+couleur[2]>700:
            couleur[3]=0
            raquette.set_at((x,y),couleur)

xp=0
yp=0
xp1=353
yp1=0
xb=44
yb=47
vx=1
vy=1
scorej1=0
scorej2=0
tr=raquette.get_size()
tb=balle.get_size()

while continuer:
    time.Clock().tick(200)
    for evenements in event.get():
        if evenements.type==QUIT:
            pygame.quit()
            sys.exit()
            continuer=0
        if evenements.type==MOUSEMOTION:
            if mouse.get_pressed()[0]:
                coord=mouse.get_pos()
                xp1=coord[0]
                yp1=coord[1]
    xb+=vx
    yb+=vy
    if yb>=353 or yb<=0:  #rebonds verticaux
        vy=-vy

    if xb>=494:
        scorej1+=1
        xb=44
        yb=47
    if xb<=0:
        scorej2+=1
        xb=44
        yb=47
    if Rect((xb,yb),tb).colliderect(Rect((xp1,yp1),tr)) or Rect((xb,yb),tb).colliderect(Rect((xp,yp),tr)):
        vx=-vx

    keyb=key.get_pressed()

    if keyb[K_UP]:
        if yp>0:
            yp=yp-1
    if keyb[K_DOWN]:
        if yp<353-110:
            yp=yp+1
    if keyb[K_LEFT]:
        if xp>0:
            xp=xp-1
    if keyb[K_RIGHT]:
        if xp<(494-76)//2:
            xp=xp+1

    if keyb[K_h]:
        if yp1>0:
            yp1=yp1-1
    if keyb[K_b]:
        if yp1<353-110:
            yp1=yp1+1
    if keyb[K_g]:
        if xp1>494//2:
            xp1=xp1-1
    if keyb[K_d]:
        if xp1<494-32:
            xp1=xp1+1

    chaine="scorej1"
    chaine="scorej2"
    font=pygame.font.SysFont("broadway",24,bold=False,italic=False)
    text=font.render(chaine,1,(255,250,245))
    fenetre.blit(fond,(0,0))
    fenetre.blit(raquette,(xp,yp))
    fenetre.blit(raquette,(xp1,yp1))
    fenetre.blit(balle,(xb,yb))
    fenetre.blit(raquette,(xp1,yp1))
    fenetre.blit(text,(30,30))
    display.flip()
quit()
