#-*- coding: utf-8 -*-

# Импортировать библиотеку под названием 'pygame'
try:
    import sys, os, random
    import pygame
    from pygame.locals import *
    # from bg import *
except ImportError as err:
    # print(str(err).split("'")[1])
    print(str(err))
    sys.exit(2)

# Объявление глобальных переменных
game = {
    'screen' : None,
    'flag'   : True,
    'clock'  : None,
    'font1'  : None,
    'font2'  : None,
}

class TGameObject():
    def __init__(self, screen):
        self.screen = screen
        self.img = []
        self.img_n = 0
        self.x = 0
        self.y = 0
    def loadimg(self, fname):
        path = 'data\img\\'
        ext = fname.split(".")[-1]
        if ext == 'png':
            self.img.append(pygame.image.load(path+fname).convert_alpha())
        else:
            self.img.append(pygame.image.load(path+fname).convert())

class TSaloon(TGameObject):
    def __init__(self, screen):
        TGameObject.__init__(self,screen)
    def __update__(self):
        screen.blit(self.x, self.y, self.img[self.img_n])

z = TSaloon("sdf")
z.loadimg("123.png")

def init(fs = false):
    global game
    pygame.init()
    pygame.font.init()
    game["screen"] = pygame.display.set_mode([800,600]])
    pygame.display.set_caption(game_info["Saloon Game"])
    game["clock"] = pygame.time.Clock()

def events():
    global game_keys, game_state
    # Анализ событий
    for e in pygame.event.get():
        if e.type == QUIT:
            game_state["done"] = False
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                if game_state['done'] == True:


#
# def move_enemy():
#     global game_info, game_state, player, enemy
#     # Управляем врагами/движущимися объектами
#     if game_info['boom'] == False:
#         enemy['y'] += enemy['ys']
#         if enemy['y'] > game_info['screen'].get_height():
#             enemy['y'] = 0 - game_img["enemy"].get_height()
#             enemy['x'] = random.randrange(0,game_info['screen'].get_width()
#             - game_img["enemy"].get_width())
#             enemy['N'] = random.randint(0,3)
#             game_img["enemy"] = pygame.image.load(
#                       'data/img/enemy'+str(enemy['N'])+'.png').convert_alpha()
#             game_img["enemy"] = pygame.transform.scale(game_img["enemy"],(100,93))
#
# def move_hero():
#     global game_keys, player
#     # Управляем персонажем
#     if game_info['boom'] == False:
#         if game_keys["up"] == True:
#             player["y"] -= player["ys"]
#         if game_keys["down"] == True:
#             player["y"] += player["ys"]
#         if game_keys["left"] == True:
#             player["x"] -= player["xs"]
#         if game_keys["right"] == True:
#             player["x"] += player["xs"]
#
# # Прогкрутка фона
# def scroll_bg():
#     global game_info, game_state, player, water, water_index
#     pass
#     # bg = game_img["bg"]
#     # # bg1 = game_img["bg"]
#     # s = int(game_info['speed'])
#     # game_info["screen"].blit(bg,[0,s],[0,s,bg.get_width(),bg.get_height()])
#     # game_info["screen"].blit(bg,[0,bg.get_height()-s],[0,0,bg.get_width(),s])
#     # # game_info["screen"].blit(bg,[0,0],[s,0,bg.get_width(),bg.get_height()])
#     # # game_info["screen"].blit(bg,[bg.get_width()-s,0],[0,0,s,bg.get_height()])
#     # bg.blit(game_info["screen"],[0,0])
#
# def draw_GUI():
#     global game_info, game_state, player, water, water_index
#     game_info["screen"].blit(game_img["counter"],(0,0))
#
# def draw_scene():
#     global game_info, game_state, player, water, water_index
#     # Отрисовка сцены - фон, сатичные объекты,
#     # динамические объекты
#     # персонаж
#     game_info["screen"].blit(game_img["bg"],(0,0))
#     # scroll_bg()
#     # game_info["screen"].blit(game_info["icon"],(10,10))
#     xm = pygame.mouse.get_pos()[0]
#     ym = pygame.mouse.get_pos()[1]
#     bm = pygame.mouse.get_pressed()
#     print(bm)
#     if game_state['menu'] == True:
#         s = "N E W"
#         s_color = (255,255,255)
#         text = game_info['font2'].render(s, True, s_color)
#         x = game_info["screen"].get_width() // 2 - text.get_width() // 2
#         y = game_info["screen"].get_height() // 2 - text.get_height() //2
#         if xm >= x and xm <= x + text.get_width() and ym >= y and ym <= y + text.get_height():
#            pygame.draw.rect(game_info["screen"],(255,0,0),[x-2,y-2,text.get_width()+2, text.get_height()+2], 1 )
#            if bm[0] == 1:
#                game_state['menu'] = False
#         game_info["screen"].blit(text,[x,y])
#
#         s = "Q U I T"
#         s_color = (255,255,255)
#         text = game_info['font2'].render(s, True, s_color)
#         x = game_info["screen"].get_width() // 2 - text.get_width() // 2
#         y = game_info["screen"].get_height() // 2 + text.get_height() //2
#         game_info["screen"].blit(text,[x,y])
#     else:
#         if game_state['pause'] == False:
#             game_info["screen"].blit(water[int(water_index)],(player['x']-18,player['y']-6))
#             water_index += 0.1
#             if water_index > len(water)-1:
#                 water_index = 0
#
#             if game_info['boom'] == False:
#                 game_info["screen"].blit(game_img["player"],(player['x'],player['y']))
#
#                 game_info["screen"].blit(game_img["enemy"],(enemy['x'],enemy['y']))
#             else:
#                 game_info["screen"].blit(game_img["boom"],(player['x'],player['y']))
#         else:
#             s = "P A U S E"
#             s_color = (255,0,0)
#             text = game_info['font1'].render(s, True, s_color)
#             x = game_info["screen"].get_width() // 2 - text.get_width() // 2
#             y = game_info["screen"].get_height() // 2 - text.get_height() //2
#             game_info["screen"].blit(text,[x,y])
#     draw_GUI()
#
# def collide():
#     global game_info,player, enemy
#     bl = player['x'] >= enemy['x'] and player['x'] <= enemy['x']+game_img['enemy'].get_width()
#     br = player['x'] + game_img['player'].get_width() >= enemy['x'] and player['x'] + game_img['player'].get_width() <= enemy['x']+game_img['enemy'].get_width()
#
#     bt = player['y'] >= enemy['y'] and player['y'] <= enemy['y']+game_img['enemy'].get_height()
#     bb = player['y'] + game_img['player'].get_height() >= enemy['y'] and player['y'] + game_img['player'].get_height() <= enemy['y']+game_img['enemy'].get_height()
#
#     if (bl or br) and (bt or bb):
#         game_info['boom'] = True
#
#     if game_info['boom'] == True:
#         game_info['boom_time'] -= 1
#         if game_info['boom_time'] <= 0:
#             game_info['boom'] = False
#             game_info['boom_time'] = game_info['boom_max_time']
#
#             enemy['y'] = 0 - game_img["enemy"].get_height()
#             enemy['x'] = random.randrange(0,game_info['screen'].get_width()
#             - game_img["enemy"].get_width())
#
#             enemy['N'] = random.randint(0,3)
#             game_img["enemy"] = pygame.image.load(
#                       'data/img/enemy'+str(enemy['N'])+'.png').convert_alpha()
#             game_img["enemy"] = pygame.transform.scale(game_img["enemy"],(100,93))
#
# def main():
#     global game_info, game_state
#     # Вызов всех функций, которые описаны выше
#     init(True) # Если True, то в полноэкранном режиме
#     while game_state["done"] == True:
#         # Обработка событий
#         events()
#         #Двигаем объекты
#         if game_state['pause'] == False:
#             move_hero()
#             move_enemy()
#             collide()
#         # Рисуем сцену
#         draw_scene()
#         # Отображаем сцену на экране
#         pygame.display.flip()
#         game_info["clock"].tick(100)
#
#     pygame.quit()
#
# if __name__ == "__main__":
#     main()
