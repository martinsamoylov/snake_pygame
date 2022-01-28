import pygame



block = 40
H = block * 15 + 2
W = block * 20 + 2

current_time = 0
time_tick = 1
fps = 100


size_h = H//block
size_w = W//block
pygame.init()
screen = pygame.display.set_mode((W,H))

