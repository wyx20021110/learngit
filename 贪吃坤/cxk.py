import pygame
from settings import settings
from collections import deque
settings = settings()
class cxk():
    def __init__(self) -> None:
        rawimage = pygame.image.load("images/cxk.png")
        newimage = pygame.transform.scale(rawimage,(settings.size,settings.size))
        self.image = newimage
        self.snake = deque()
        self.snake.append((2,settings.scopey[0]))
        self.snake.append((1,settings.scopey[0]))
        self.snake.append((0,settings.scopey[0]))
            
                


