# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
import fielddraw
import pygame
import settings
import storage
import snake
import engine

done = False

s = snake.Snakes()

clock = settings.pygame.time.Clock()
font = settings.pygame.font.SysFont("Arial", 18)
key_up = False
key_l = False
key_r = False
pause = False
key_down = False

key = "r"

def update_fps():
    fps = int(clock.get_fps())
    fps_text = font.render(f'{fps}     kill: {settings.kill} '
                           f'level: {settings.level}'
                           f'time = {storage.current_time//100/10}',
                           1, settings.pygame.Color("black"))


    return fps_text
tick = 0

while not done:

    if storage.current_time == 0:
        storage.current_time = pygame.time.get_ticks()
        storage.time_tick = 1
    else:
        storage.time_tick = (pygame.time.get_ticks() - storage.current_time) / (1000/60)

        storage.current_time = pygame.time.get_ticks()


    for event in settings.pygame.event.get():
        if event.type == settings.pygame.QUIT:
            done = True
        elif event.type == settings.pygame.KEYDOWN:
            if event.key == settings.pygame.K_LEFT:
                s.razver('l')
            elif event.key == settings.pygame.K_RIGHT:
                s.razver('r')
            elif event.key == pygame.K_p:
                pause = not pause
            elif event.key == settings.pygame.K_DOWN:
                s.razver('d')
            elif event.key == settings.pygame.K_UP:
                s.razver('u')
        elif event.type == settings.pygame.KEYUP:
            if event.key == settings.pygame.K_LEFT:
                key_l = False
            elif event.key == settings.pygame.K_RIGHT:
                key_r = False
            elif event.key == settings.pygame.K_DOWN:
                key_down = False
    settings.screen.fill((50, 50, 50))
    fielddraw.draw()

    if s.move() == False:
        break
    s.draw()




    clock.tick(storage.fps)
    settings.pygame.display.update()
    settings.pygame.display.flip()
settings.pygame.quit()
