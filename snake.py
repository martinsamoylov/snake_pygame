import settings
import pygame
from Point import Point
import random
class Snakes:
    def __init__(self):
        self.mp = [Point(1, 5), Point(1, 6), Point(1, 7)]
        self.time = pygame.time.get_ticks()
        self.key = "r"
        self.key_queue = []
        self.apple = self.createapple()

    def draw(self):
        for p in self.mp:
            s = settings.block
            zz = 10
            zzh = 5
            z = s - 2*zz
            zh = s - 2*zzh
            pygame.draw.rect(settings.screen, (0,200,0), (p.x * s + zz,p.y *s + zz,z,z))


        p = self.mp[0]
        pygame.draw.rect(settings.screen, '#006400', (p.x * s + zzh - 1, p.y * s + zzh - 1, zh + 2, zh + 2))
        pygame.draw.rect(settings.screen, (200, 0, 0), (self.apple.x * s+2, self.apple.y * s+2, s-4, s-4))
    def move(self):
        t = pygame.time.get_ticks() - self.time

        if t < 500:
            return
        self.time = pygame.time.get_ticks()

        p = self.mp[0]
        x = p.x
        y = p.y

        if len(self.key_queue) > 0:
            self.key = self.key_queue.pop(0)

        if self.key == 'r':
            x = x + 1
        elif self.key == 'd':
            y = y + 1
        elif self.key == 'l':
            x = x - 1
        elif self.key == 'u':
            y = y - 1

        if x > settings.size_w - 1:
            x = 0
        if x <= -1:
            x = settings.size_w - 1
        if y > settings.size_h - 1:
            y = 0
        if y <= -1:
            y = settings.size_h - 1

        newp = Point(x, y)
        if newp in self.mp:
            return False
        self.mp.insert(0, newp)

        if newp == self.apple:
            self.apple = self.createapple()
        else:
            del self.mp[-1]

        return True



    def razver(self,key):
        if len(self.key_queue) > 0:
            k = self.key_queue[-1]
        else:
            k = self.key

        if k == 'r' and key == 'l':
            return
        if k == 'l' and key == 'r':
            return
        if k == 'u' and key == 'd':
            return
        if k == 'd' and key == 'u':
            return
        if len(self.key_queue) > 0:
            if key == self.key_queue[-1]:
                return
        self.key_queue.append(key)
    def createapple(self):
        a = random.randint(0, settings.size_w - 1)
        b = random.randint(0, settings.size_h - 1)
        p = Point(a,b)

        if p in self.mp:
            return self.createapple()
        return p









































































































































































































































































































































































































