import pygame
widht = 800
height = 700


GREEN = (0,255,0)


class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.image = pygame.Surface([120,20])
        pygame.draw.rect(self.image, GREEN,[0,0,120,20])
        self.rect = self.image.get_rect()

    def moveRight(self):
        self.rect.x += 10
        if self.rect.x >= (widht - 120):
            self.rect.x = widht - 120

    def moveLeft(self):
        self.rect.x -= 10
        if self.rect.x <= 0:
            self.rect.x = 0
