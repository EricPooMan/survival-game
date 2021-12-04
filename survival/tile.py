import pygame
import os

cur = os.path.dirname(__file__)

class Tile(pygame.sprite.Sprite):
    def __init__(self, tilename, pos, fill = False):
        pos = pos.split(sep = " ")
        position = [(int(pos[0]) * 16), (int(pos[1]) * 16)]

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(cur + "\\assets\\images\\" + tilename)
        self.imagepath = cur + "\\assets\\images\\" + tilename
        self.rect = self.image.get_rect()
        self.rect.x = int(position[0])
        self.rect.y = int(position[1])

        self.move_x = 0
        self.move_y = 0

    def update(self):
        self.rect.x += self.move_x
        self.rect.y += self.move_y

    
