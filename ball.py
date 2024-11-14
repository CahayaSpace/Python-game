import pygame
import random

GRAY = (220, 220, 220)
WIDTH = 800
HEIGHT = 700

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        # Membuat gambar bola
        self.image = pygame.Surface([20, 20])
        pygame.draw.rect(self.image, GRAY, [0, 0, 20, 20])
        self.rect = self.image.get_rect()
        
        # Kecepatan awal bola pada sumbu X dan Y
        self.speed_x = random.randint(3, 7)
        self.speed_y = random.randint(4, 8)

    def initialPos(self):
        # Menentukan posisi awal bola di layar
        self.rect.x = (WIDTH / 2) - 10
        self.rect.y = HEIGHT - 300

    def update(self):
        # Menggerakkan bola dengan kecepatan yang ditentukan
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def bounceX(self):
        # Membalik arah kecepatan di sumbu X
        self.speed_x = -self.speed_x

    def bounceY(self):
        # Membalik arah kecepatan di sumbu Y
        self.speed_y = -self.speed_y
