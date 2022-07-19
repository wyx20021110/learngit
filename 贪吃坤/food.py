import pygame
from soupsieve import select
from settings import settings
import random


class food():
    def __init__(self) -> None:
        self.image1 = pygame.transform.scale(pygame.image.load('images/lq.png'),(settings().size,settings().size))
        self.image2 = pygame.transform.scale(pygame.image.load('images/ji.png'),(settings().size,settings().size))
    def createfood1(self,x,y,screen):
        screen.blit(self.image1,(x,y))
    def createfood2(self,x,y,screen):
        screen.blit(self.image2,(x,y))
        
        





