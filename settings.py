import pygame



H = 401
W = 401
block = 40

current_time = 0
time_tick = 1
fps = 100


size = H//block
pygame.init()
screen = pygame.display.set_mode((W,H))

