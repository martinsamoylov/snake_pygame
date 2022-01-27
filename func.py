import pygame
from pygame import gfxdraw

def len(a, b):
    return ((a.x - b.x) ** 2 + (a.y - b.y) ** 2) ** .5

def draw_circle_alpha(surface, color, center, radius):
    target_rect = pygame.Rect(center, (0, 0)).inflate((radius * 2, radius * 2))
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.circle(shape_surf, color, (radius, radius), radius)
    surface.blit(shape_surf, target_rect)

def draw_circle(surface, x, y, radius, color):
    gfxdraw.aacircle(surface, int(x), int(y), int(radius), color)

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