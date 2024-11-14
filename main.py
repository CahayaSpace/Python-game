import pygame
import sys

# Inisialisasi pygame
pygame.init()

# Ukuran layar
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brick Breaker")

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Variabel game
paddle_width = 100
paddle_height = 10
paddle_speed = 10
ball_radius = 10
ball_speed_x = 5
ball_speed_y = -5
brick_rows = 5
brick_columns = 20
brick_margin = 2  # Margin antar brick

# Ukuran brick dengan margin
brick_width = (WIDTH - (brick_columns + 1) * brick_margin) // brick_columns
brick_height = 30

# Objek Paddle
paddle = pygame.Rect(WIDTH // 2 - paddle_width // 2, HEIGHT - 30, paddle_width, paddle_height)

# Objek Bola
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, ball_radius * 2, ball_radius * 2)

# Objek Brick
bricks = []
for row in range(brick_rows):
    brick_row = []
    for col in range(brick_columns):
        brick_x = col * (brick_width + brick_margin) + brick_margin
        brick_y = row * (brick_height + brick_margin) + brick_margin
        brick = pygame.Rect(brick_x, brick_y, brick_width, brick_height)
        brick_row.append(brick)
    bricks.append(brick_row)

# Fungsi untuk menggambar objek
def draw():
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    for row in bricks:
        for brick in row:
            pygame.draw.rect(screen, BLUE, brick)
    pygame.display.flip()

# Game Loop
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Gerakan Paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.x += paddle_speed

    # Gerakan Bola
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Pantulan bola di dinding
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed_x *= -1
    if ball.top <= 0:
        ball_speed_y *= -1

    # Pantulan bola di paddle
    if ball.colliderect(paddle):
        ball_speed_y *= -1

    # Pantulan bola di bricks
    for row in bricks:
        for brick in row:
            if ball.colliderect(brick):
                ball_speed_y *= -1
                row.remove(brick)
                break

    # Bola jatuh ke bawah
    if ball.bottom >= HEIGHT:
        running = False  # Game over

    # Periksa kemenangan
    if all(len(row) == 0 for row in bricks):
        print("You win!")
        running = False

    draw()

pygame.quit()
sys.exit()
