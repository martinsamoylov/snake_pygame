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