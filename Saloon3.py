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
    "luck" : 0.5,
    "bullets" : 8,
    "shoot_time" : 10,
    "comp_hp" : 100,
    "comp_damage" : 10,
    "comp_delay" : 10,
    "comp_xy"   : [10,10],
    "screen"  : None,
    "clock"   : None,
    "mouse_cur" : None,
    "mouse_xy"  : [0,0],
    "bullet_hole" : None,

    "hit_player": False,
    "hit_enemy": False,

    "gameover": False,

    "bullet_img": None,
    "font": None,

    "earthquake": False,
    "earthquake_maxtime": 10,
    "earthquake_time": 10,

    "gun1": None,
    "gun2": None,
    "gun3": None,
}

# Создаем классы объектов
class TGameObject():
    def __init__(self,screen):
        self.screen = screen
        self.img = [] # массив для изображений
        self.img_n = 0 # номер отображаемой картинки
        self.xy = [0,0] # координаты вывода картинки на экран
        self.font = pygame.font.Font(None, 25)
    def update(self):
        if game["earthquake"] == True:
            x = self.xy[0] + random.randint(-10,10)
            y = self.xy[1] + random.randint(-10,10)
            game["earthquake_time"] -= 0.1
            if game["earthquake_time"] <= 0:
                game["earthquake_time"] = game["earthquake_maxtime"]
                game["earthquake"] = False
            self.screen.blit(self.img[self.img_n], [x,y])
        else:
            self.screen.blit(self.img[self.img_n], self.xy)
    def loadimg(self, fname):
        path = 'data\img\\'
        ext = fname.split('.')[-1]
        if ext == 'png':
            self.img.append(pygame.image.load(path+fname).convert_alpha())
        else:
            self.img.append(pygame.image.load(path+fname).convert())
class TMan(TGameObject):
    def __init__(self, screen):
        TGameObject.__init__(self, screen)
        # 0 - не видно, сидит внутри
        # 1 - подошел к случайному окну
        # 2 - открыл окно
        # 3 - поднял оружие
        # 4 - Выстрелил
        # 5 - сдается или убили
        self.state = 1
        self.maxstate = 5
        self.time = 10
        self.maxtime = 10
        self.new_window()
    def update(self, man2):
        if self.state !=0 :
            if man2.xy == self.xy:
                self.new_window()
            else:
                self.screen.blit(self.img[self.img_n],self.xy)
        self.countdown()

    def new_window(self):
        self.img_n = 0
        self.state = 0
        r = random.randint(1,5)
        if r ==1 :
            self.xy = [75,70]
        elif r == 2:
            self.xy = [555,70]
        elif r == 3 :
            self.xy = [75,275]
        elif r ==4:
            self.xy = [555,275]

    def countdown(self):
        self.time -= 0.05
        if self.time <=0:
            self.time = random.randint(4,self.maxtime)
            self.state += 1

            if self.state > self.maxstate:
                self.state = 0

            if self.state == 0:
                self.img_n = 0
                print("меня нету")
            if self.state == 1:
                self.img_n = 0
                print("подошел к окну")
            if self.state == 2:
                self.img_n = 1
                print("поднял оружие")
            if self.state == 3:
                self.img_n = 2
                print("поднял второе оружие")
            if self.state == 4:
                self.img_n = 3
                print("Выстрелил в игрока")
                pygame.mixer.Sound.play(game['gun1'])
                game["hp"] -=10
                game["earthquake"] = True
                if game["hp"] <=0:
                    game["gameover"] = True
            if self.state == 5:
                self.img_n = 3
                print("Ухожу внутрь салона")
                self.new_window()
            if self.state == 6:
                self.img_n = 0
                print("Ухожу внутрь салона")
                self.new_window()
            # выводим таймер на экран
            s = str(int(self.time))
            s_color = (255,255,255)
            text = self.font.render(s, True, s_color)
            xy = [self.xy[0]+70, self.xy[1]+20]
            self.screen.blit(text, xy)



class TSaloon(TGameObject): # собственно saloon
    def update(self):
        # Рисуем общий фон
        TGameObject.update(self)
        # Рисуем дверь
        if game["earthquake"] == True:
            game["earthquake_time"] -= 0.1
            if game["earthquake_time"] <= 0:
                game["earthquake_time"] = game["earthquake_maxtime"]
                game["earthquake"] = False
            x = 50 + random.randint(-10,10)
            y = 50 + random.randint(-10,10)
            xy = [x, y]
            self.screen.blit(self.img[3],xy)

            x = 50 + random.randint(-10,10)
            y = 260 + random.randint(-10,10)
            xy = [x, y]
            self.screen.blit(self.img[3],xy)

            x = 534 + random.randint(-10,10)
            y = 50 + random.randint(-10,10)
            xy = [x, y]
            self.screen.blit(self.img[3],xy)

            x = 534 + random.randint(-10,10)
            y = 260 + random.randint(-10,10)
            xy = [x, y]
            self.screen.blit(self.img[3],xy)

            x =  random.randint(-10,10)
            y =  random.randint(-10,10)
            xy = [x, y]
            self.screen.blit(self.img[4],xy)

        else:
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



pygame.init()
game["clock"] = pygame.time.Clock()
# size=pygame.display.list_modes()[0]
# game["screen"] = pygame.display.set_mode(size, FULLSCREEN)
size=[722,541]
game["screen"] = pygame.display.set_mode(size)
game["saloon"] = TSaloon(game["screen"])
game['saloon'].loadimg('saloon1.png') # 0
game['saloon'].loadimg('door1.png')   # 1
game["saloon"].loadimg("window1.png") # 2
game["saloon"].loadimg("window2.png") # 3
game["saloon"].loadimg("saloon2.png") # 4

game["man1"] = TMan(game["screen"])
game["man1"].loadimg('man1.1.png')
game["man1"].loadimg('man1.2.png')
game["man1"].loadimg('man1.3.png')
game["man1"].loadimg('man1.4.png')
game["man1"].loadimg('window1.png')

game["man2"] = TMan(game["screen"])
game["man2"].loadimg('man2.1.png')
game["man2"].loadimg('man2.2.png')
game["man2"].loadimg('man2.3.png')
game["man2"].loadimg('man2.4.png')
game["man2"].loadimg('window1.png')

game["mouse_cur"] = pygame.image.load("data\img\mouse.png").convert_alpha()
game["bullet_hole"] = pygame.image.load("data\img\\boom.png").convert_alpha()
game["bullet_img"] = pygame.image.load("data\img\\bullet.png").convert_alpha()

game['font'] = pygame.font.Font(None, 25)

game['gun1'] = pygame.mixer.Sound('data\snd\gun1.wav')
game['gun2'] = pygame.mixer.Sound('data\snd\gun2.wav')
game['gun3'] = pygame.mixer.Sound('data\snd\gun3.wav')




def comp():
    global game
    pass

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
        if e.type == MOUSEBUTTONDOWN:
            if (game['mouse_xy'][1] >= game['screen'].get_height() - (game['bullet_img'].get_height() + 30)):
                game['bullets'] = 8
                pygame.mixer.Sound.play(game['gun3'])
            elif game['bullets'] > 0:
                pygame.mixer.Sound.play(game['gun1'])

                game["earthquake"] = True

                game['saloon'].img[-1].blit(game["bullet_hole"], game['mouse_xy'])
                print("Выстрел")
                # Уменьшаем кол-во патронов
                game['bullets'] -= 1
                # Проверяем попадание в 1-го человечка
                lb = game['mouse_xy'][0] >= game['man1'].xy[0]
                rb = game['mouse_xy'][0] <= game['man1'].xy[0] + game['man1'].img[0].get_width()

                tb = game['mouse_xy'][1] >= game['man1'].xy[1]
                bb = game['mouse_xy'][1] <= game['man1'].xy[1] + game['man1'].img[0].get_height()

                if (lb == True and rb ==True and tb ==True and bb == True):
                    print('\t П О П А Л !!!!!')
                    game["score"] += 10
                    print('\t\t %s'%(game["score"]))
                    # game["man1"].img_n = 4
                    game["man1"].state = 6
                    # game["man1"].new_window()

                # Проверяем попадание в 2-го человечка
                lb = game['mouse_xy'][0] >= game['man2'].xy[0]
                rb = game['mouse_xy'][0] <= game['man2'].xy[0] + game['man2'].img[0].get_width()

                tb = game['mouse_xy'][1] >= game['man2'].xy[1]
                bb = game['mouse_xy'][1] <= game['man2'].xy[1] + game['man2'].img[0].get_height()

                if (lb == True and rb ==True and tb ==True and bb == True):
                    print('\t П О П А Л !!!!!')
                    game["score"] += 10
                    print('\t\t %s'%(game["score"]))
                    game["man1"].state = 6
                    # game["man2"].new_window()
            else:
                pygame.mixer.Sound.play(game['gun2'])


def gui(screen):
    global game
    # Рисуем поле для вывода информации о пулях и т.п.
    color = (0,0,0)
    h = game['bullet_img'].get_height() + 5
    w = game['screen'].get_width()
    x = 0
    y = game['screen'].get_height() - h
    pygame.draw.rect(game['screen'],color,[x,y,w,h])
    y = game['screen'].get_height() - game['bullet_img'].get_height() - 3
    x = 0
    for i in range(game['bullets']):
        x += game['bullet_img'].get_width() + 5
        game['screen'].blit(game['bullet_img'],[x,y])

    # Выводим очки здоровья
    s = 'Life - ' + str(game['hp'])
    color = (255,255,255)
    text = game['font'].render(s, True, color)
    y = game['screen'].get_height() - game['bullet_img'].get_height()
    x = game['screen'].get_width() - text.get_width() - 10
    game['screen'].blit(text, [x,y])

    # Выводим очки
    s = 'Score - ' + str(game['score'])
    color = (255,255,255)
    text = game['font'].render(s, True, color)
    y = game['screen'].get_height() - game['bullet_img'].get_height()
    x = game['screen'].get_width() // 2 - text.get_width() //2
    game['screen'].blit(text, [x,y])

    game["mouse_xy"][0] = pygame.mouse.get_pos()[0] - game['mouse_cur'].get_width() // 2
    game["mouse_xy"][1] = pygame.mouse.get_pos()[1] - game['mouse_cur'].get_height() // 2
    game['screen'].blit(game['mouse_cur'],game['mouse_xy'])

def render(screen):
    global game
    game['screen'].fill([0,0,0])
    game['man1'].update(game['man2'])
    game['man2'].update(game['man1'])
    game['saloon'].update()
    gui(game['screen'])
    pygame.display.flip()

# Основная функция
def main():
    global game
    while game["flag"] == True:
        events()
        render(game['screen'])
    pygame.quit()

if __name__ == "__main__":
    main()
