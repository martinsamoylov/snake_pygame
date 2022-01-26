import pygame

def set_alphas(color):
    # if color == (255,255,0): # magenta means clear
    #     return (0,0,0,0)
    # if color == (0,255,255): # cyan means shadow
    #     return (0,0,0,128)
    r,g,b = color
    return (r,g,b,125) # otherwise use the solid color from the image.

def change_alpha(img,alpha=255):
  width,height=img.get_size()
  for x in range(0,width):
    for y in range(0,height):
      r,g,b,old_alpha=img.get_at((x,y))
      if old_alpha>0:
        img.set_at((x,y),(r,g,b,alpha))
  return img

H = 401
W = 401
block = 40

size = H//block

pygame.init()
screen = pygame.display.set_mode((W,H))

bg = pygame.image.load("data/bg3.jpg.png")
pushka = pygame.image.load("data/pushka1.png")
shild120 = pygame.image.load("data/shit.png")
shild60 = pygame.image.load("data/shit.png")
shild20 = pygame.image.load("data/shit.png")
shild255 = pygame.image.load("data/shit.png")
shield_gift = pygame.image.load("data/shield_gift.png")


shild120 = change_alpha(shild120, 120)
shild60 = change_alpha(shild60, 60)
shild20 = change_alpha(shild20, 20)



# for row in range(shit.get_height()):
#     for col in range(shit.get_width()):
#         shit.set_at((row, co

#                     l), set_alphas(shit.get_at((row, col))[:3]))
floor = H - 240
fireball = pygame.image.load("data/fireball.png")
fireball_gift = pygame.image.load("data/fireball_40.png")
heart_gift = pygame.image.load("data/heart_40.png")
gift_B0X = pygame.image.load('data/gift.png')
gift_BOX_25 = pygame.image.load('data/gift_25.png')

circles = []

for i in range(4,15):
    circles.append(change_alpha(pygame.image.load("data/cc10.png"), i**2 -2 ))

kill = 0
level = 1
