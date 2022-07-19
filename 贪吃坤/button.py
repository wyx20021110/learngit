import pygame

class button():
    def __init__(self,screen) -> None:
        self.width,self.height = 300,100
        self.textcolor = (255,255,255)
        self.buttoncolor = (0,255,0)
        self.font = pygame.font.SysFont("SimHei",48)
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = screen.get_rect().center
        self.screen = screen
    def createbutton(self,msg):
        msgimg = self.font.render(msg,True,"red")
        msgrect = msgimg.get_rect()
        msgrect.center = self.rect.center
        pygame.draw.rect(self.screen,'yellow',self.rect,width = 0)   
        self.screen.blit(msgimg,msgrect)     