import settings
import pygame
def draw():
    lines = 100
    color = pygame.Color(100, 200,200)
    x = 0

    for _ in range(lines):
        p1 = (x,1000)
        p2 = (x, 0)
        x += settings.block
        pygame.draw.line(settings.screen, color, p1, p2)


    for y in range(0, settings.H, settings.block):
        p1 = (0,y)
        p2 = (1000, y)
        pygame.draw.line(settings.screen, color, p1, p2)
