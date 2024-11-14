import pygame
from paddle import Paddle
from ball import Ball
from brick import Brick

pygame.init()
pygame.mixer.init()

# Load suara pantulan
bounce_sound = pygame.mixer.Sound("asset/bounce.wav")

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brick Breaker")

# Warna
GREEN = (0, 255, 0)
BLUE = (50, 100, 200)
RED = (255, 0, 0)
GRAY = (220, 220, 220)

FPS = 60
clock = pygame.time.Clock()

# Objek Paddle
paddle = Paddle()
paddle.rect.x = (WIDTH / 2) - 60
paddle.rect.y = HEIGHT - 60

# Objek Bola
ball = Ball()
ball.initialPos()

# Grup Sprite
allSprites = pygame.sprite.Group()
allSprites.add(paddle)
allSprites.add(ball)

# Grup Brick
allBricks = pygame.sprite.Group()

# Fungsi untuk membuat brick
def instBricks(c, r):
    for i in range(c):
        for j in range(r):
            brick = Brick(RED)
            brick.rect.x = 2 + i * 110
            brick.rect.y = 2 + j * 30
            allBricks.add(brick)
            allSprites.add(brick)

# Inisialisasi brick
instBricks(7, 9)

start = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Gerakan Paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        start = True
    if keys[pygame.K_RIGHT]:
        paddle.moveRight()
    if keys[pygame.K_LEFT]:
        paddle.moveLeft()

    # Mulai gerakan bola saat space ditekan
    if start:
        allSprites.update()

        # Pantulan dinding
        if ball.rect.right >= WIDTH or ball.rect.left <= 0:
            ball.bounceX()
            bounce_sound.play()  # Mainkan suara saat pantulan dinding

        if ball.rect.top <= 0:
            ball.bounceY()
            bounce_sound.play()  # Mainkan suara saat pantulan dinding atas

        # Pantulan paddle
        if ball.rect.colliderect(paddle.rect):
            ball.bounceY()
            bounce_sound.play()  # Mainkan suara saat pantulan paddle

        # Pantulan brick
        ballHitList = pygame.sprite.spritecollide(ball, allBricks, False)
        for brick in ballHitList:
            # Cek posisi relatif bola terhadap brick untuk memutuskan arah pantulan
            if abs(ball.rect.bottom - brick.rect.top) < 10 and ball.speed_y > 0:
                ball.bounceY()
            elif abs(ball.rect.top - brick.rect.bottom) < 10 and ball.speed_y < 0:
                ball.bounceY()
            elif abs(ball.rect.right - brick.rect.left) < 10 and ball.speed_x > 0:
                ball.bounceX()
            elif abs(ball.rect.left - brick.rect.right) < 10 and ball.speed_x < 0:
                ball.bounceX()
            
            bounce_sound.play()  # Mainkan suara saat pantulan brick
            brick.kill()

    # Gambar layar
    screen.fill(BLUE)
    allSprites.draw(screen)
    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
