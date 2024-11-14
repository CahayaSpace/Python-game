import pygame

class Brick(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()

        self.image = pygame.Surface([100,20])
        pygame.draw.rect(self.image, color, [0,0,100,20])
        self.rect = self.image.get_rect()