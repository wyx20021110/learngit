
import pygame,sys,time,random
from collections import deque
import settings
from cxk import cxk
from food import food
from button import button


pygame.init()
settings = settings.settings()
cxk = cxk()
pos_x = 1
pos_y = 0
bgimg = pygame.transform.scale(pygame.image.load("images/bgimg.jpg"),(settings.width,settings.height))
start = False
screen = pygame.display.set_mode((settings.width,settings.height))
pygame.display.set_caption("贪吃坤")
clock = pygame.time.Clock()
b = True
food = food()
foodexist = False
gameover = False
pygame.mixer.music.load("audio/bgm.mp3")
pygame.mixer.music.play()
over = False
while True:
    clock.tick(5)
    screen.fill(settings.color)
    screen.blit(bgimg,(0,0))
    if start == False:
        button(screen).createbutton("开始贪吃坤")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            if button(screen).rect.collidepoint(x,y):
                start = True


        elif event.type == pygame.KEYDOWN and start == True:
            if event.key in (pygame.K_UP, pygame.K_w):
                 
                if b and not pos_y:
                    pos_x = 0
                    pos_y = -1
                    b = False
            elif event.key in (pygame.K_s, pygame.K_DOWN):
                if b and not pos_y:
                    pos_x = 0
                    pos_y = 1
                    b = False
            elif event.key in (pygame.K_a, pygame.K_LEFT):
                if b and not pos_x:
                    pos_x = -1
                    pos_y = 0
                    b = False
            elif event.key in (pygame.K_d, pygame.K_RIGHT):
                if b and not pos_x:
                    pos_x = 1
                    pos_y = 0
                    b = False
    
    b = True
    if start == True:
        for x in range(settings.size,settings.width,settings.size):
            pygame.draw.line(screen,'black',(x,0),(x,settings.height))  
        for y in range(settings.size,settings.height,settings.size):
            pygame.draw.line(screen,'black',(0,y),(settings.width,y))
        for i in cxk.snake:
            screen.blit(cxk.image,(settings.size*i[0],settings.size*i[1]))
        while not foodexist:
            lq = (random.randint(settings.scopex[0],settings.scopex[1]),random.randint(settings.scopey[0],settings.scopey[1]))
            if lq in cxk.snake:
                continue
            foodexist = True
        if not gameover:    
            food.createfood2(lq[0]*settings.size,lq[1]*settings.size,screen)
            next_s = (cxk.snake[0][0]+pos_x,cxk.snake[0][1]+pos_y)
            if next_s[0] > settings.scopex[1] or next_s[0]< 0 or next_s[1]> settings.scopey[1] or next_s[1]<0:
                gameover = True
            if next_s not in cxk.snake:
                cxk.snake.appendleft(next_s)
                if not next_s == lq:
                    cxk.snake.pop()
                else:
                    foodexist = False    
            else:
                gameover = True 
    if gameover and not over:  
        
        pygame.display.update()
        pygame.mixer.music.load("audio/你干嘛.mp3")
        pygame.mixer.music.set_volume(1) 
        pygame.mixer.music.play(1)
        time.sleep(3)
        over = True

    pygame.display.update() 

   