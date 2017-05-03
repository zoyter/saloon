# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import random
import os
import sys

game = {
    "state" : "loading",
    "flag"  : True,
    "level" : 1,
    "hp"    : 100,
    "score" : 0,
    "player_level" : 1,
    "player_xy" : [10,10],
    "luck" : 0.5,
    "bullets" : 8,
    "shoot_time" : 10,
    "comp_hp" : 100,
    "comp_damage" : 10,
    "comp_delay" : 10,
    "comp_xy"   : [10,10],
    "screen"  : None,
    "clock"   : None,
}

# --------------------------------------
# Игровые объекты
class TGameObject():
    def __init__(self, screen): # инициализация
        self.screen = screen # экран
        self.img = [] # массив для картинок
        self.img_n = 0 # номер картинки, которую рисуем на экране
        self.xy = [0,0] # координаты вывода картинки
        self.font = pygame.font.Font(None, 25) # шрифт, которым можно что-н написать

    def update(self): # обновление
        self.screen.blit(self.img[self.img_n],self.xy)

    def loadimg(self, fname): # загрузка картинки
        path = 'data\img\\'
        ext = fname.split(".")[-1]
        if ext == 'png':
            self.img.append(pygame.image.load(path+fname).convert_alpha())
        else:
            self.img.append(pygame.image.load(path+fname).convert())

class TSaloon(TGameObject): # собственно saloon
    def __init__(self, screen):
        TGameObject.__init__(self,screen)
    def update(self):
        # Рисуем общий фон
        TGameObject.update(self)
        # Рисуем дверь
        x = self.img[self.img_n].get_width() // 2 - self.img[self.img_n+1].get_width() // 2
        y = self.img[self.img_n].get_height() - self.img[self.img_n+1].get_height() - 30
        xy = [x, y]
        self.img_n += 1
        self.screen.blit(self.img[self.img_n],xy)

        # Рисуем окно 2.1
        x = 50
        y = 50
        xy = [x, y]
        self.img_n += 2
        self.screen.blit(self.img[self.img_n],xy)

        # Рисуем окно 1.1
        x = 50
        y = 260
        xy = [x, y]
        self.img_n += 0
        self.screen.blit(self.img[self.img_n],xy)

        # Рисуем окно 2.2
        x = 534
        y = 50
        xy = [x, y]
        self.screen.blit(self.img[self.img_n],xy)

        # Рисуем окно 1.2
        x = 534
        y = 260
        xy = [x, y]
        self.screen.blit(self.img[self.img_n],xy)

        # Рисуем балки
        x = 0
        y = 0
        xy = [x, y]
        self.img_n += 1
        self.screen.blit(self.img[self.img_n],xy)

        self.img_n = 0


class TMan(TGameObject):
    def __init__(self, screen):
        TGameObject.__init__(self,screen)
        # Состояние противника:
        #   0 - сидит внутри
        #   1 - подошел к случайному окну и ждет
        #   2 - открыл окно и ждет
        #   3 - поднял оружие и выстрелил
        #   4 - убит/сдается
        self.state = 0
        self.maxstate = 4
        # таймер обратного отсчета для появления в новом месте
        self.maxtimer = 10
        self.timer = 10
    def new_window(self):
        r = random.randint(1,5)
        if r == 1:
            self.xy = [75,70]
        elif r == 2:
            self.xy = [555,70]
        elif r == 3:
            self.xy = [75,275]
        elif r == 4:
            self.xy = [555,275]
    def countdown(self):
        # Уменьшаем таймер
        self.timer -=0.1
        # Если таймер дошел до нуля
        if self.timer<=0:
            # заводим опять таймер
            self.timer = random.randint(4,self.maxtimer)
            # self.timer = self.maxtimer
            self.state += 1
            if self.state > self.maxstate:
                self.state = 0
            # Проверям в каком состоянии сейчас противник
            if self.state == 0: # сидит внутри
                self.img_n = 0
            if self.state == 1: # подходит к окну
                self.img_n = 0
            if self.state == 2: # один пистолет
                self.img_n = 1
            if self.state == 3: # два пистолета
                self.img_n = 2
                # self.new_window()
            if self.state == 4: # сдается
                self.img_n = 3
                self.new_window()

        s = str(int(self.timer))
        s_color = (255,255,255)
        text = self.font.render(s, True, s_color)
        xy = [self.xy[0] + 70, self.xy[1] + 20]
        self.screen.blit(text,xy)
    def update(self):
        if self.state != 0:
            self.screen.blit(self.img[self.img_n],self.xy)
        self.countdown()


# -----------------------------------------------

pygame.init()

game["clock"] = pygame.time.Clock()
# size=pygame.display.list_modes()[0]
# game["screen"] = pygame.display.set_mode(size, FULLSCREEN)
size=[722,541]
game["screen"] = pygame.display.set_mode(size)
game["saloon"] = TSaloon(game["screen"])
game["saloon"].loadimg("saloon1.png")
game["saloon"].loadimg("door1.png")
game["saloon"].loadimg("window1.png")
game["saloon"].loadimg("window2.png")
game["saloon"].loadimg("saloon2.png")

game["man1"] = TMan(game["screen"])
game["man1"].loadimg("man1.1.png")
game["man1"].loadimg("man1.2.png")
game["man1"].loadimg("man1.3.png")
game["man1"].loadimg("man1.4.png")
game["man1"].xy = [75,70]


def comp():
    global game

# Действия игрока
def player():
    global game
    pass

# Обработка событий
def events():
    global game
    for e in pygame.event.get():
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                game["flag"] = False
            if e.key == K_SPACE:
                game["man1"].new_window()

def gui(screen):
    global game
    pass

def render(screen):
    global game
    game['screen'].fill([0,0,0])
    game["man1"].update()
    game["saloon"].update()
    pygame.display.flip()

# Основная функция
def main():
    global game
    while game["flag"] == True:
        events()
        render(game["screen"])
        game["clock"].tick(100)
    pygame.quit()

if __name__ == "__main__":
    main()
