import pygame



class Background(pygame.sprite.Sprite):

    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        
    def update(self, screen):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -= 1
        if key[pygame.K_RIGHT]:
            self.rect.x += 1
        if key[pygame.K_UP]:
            self.rect.y -= 1
        if key[pygame.K_DOWN]:
            self.rect.y += 1
