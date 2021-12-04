import pygame
import os

pth = os.path.dirname(__file__)

class Player(pygame.sprite.Sprite):

    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load(pth + "\\assets\\images\\hero.png")
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.move_x = 0
        self.move_y = 0

    def update(self):
        self.rect.x += self.move_x
        self.rect.y += self.move_y



        
