import pygame
class settings():
    def __init__(self) -> None:
        self.width = 900
        self.height = 600
        self.color = (234,233,234)
        self.size = 30
        self.scopex = (0,self.width//self.size-1)
        self.scopey = (0,self.height//self.size-1)
 