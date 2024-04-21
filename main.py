
import pygame
import random

# Initializing Pygame
pygame.init()

# Setting up the screen
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong Game")

# Game variables
paddle_width, paddle_height = 15, 90
ball_radius = 10
ball_speed_x, ball_speed_y = 7 * random.choice((1, -1)), 7 * random.choice((1, -1))
paddle_speed = 7
score_player1, score_player2 = 0, 0
font = pygame.font.Font(None, 74)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddles and ball
paddle1 = pygame.Rect(10, height//2 - paddle_height//2, paddle_width, paddle_height)
paddle2 = pygame.Rect(width - paddle_width - 10, height//2 - paddle_height//2, paddle_width, paddle_height)
ball = pygame.Rect(width//2 - ball_radius, height//2 - ball_radius, ball_radius*2, ball_radius*2)

# Game loop
running = True
while running:
    # Handling events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Moving paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1.top > 0:
        paddle1.y -= paddle_speed
    if keys[pygame.K_s] and paddle1.bottom < height:
        paddle1.y += paddle_speed
    if keys[pygame.K_UP] and paddle2.top > 0:
        paddle2.y -= paddle_speed
    if keys[pygame.K_DOWN] and paddle2.bottom < height:
        paddle2.y += paddle_speed

    # Moving the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Collision with top and bottom
    if ball.top <= 0 or ball.bottom >= height:
        ball_speed_y *= -1

    # Collision with paddles
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed_x *= -1

    # Scoring
    if ball.left <= 0:
        score_player2 += 1
        ball.center = (width//2, height//2)
        ball_speed_x *= random.choice((1, -1))
    if ball.right >= width:
        score_player1 += 1
        ball.center = (width//2, height//2)
        ball_speed_x *= random.choice((1, -1))

    # Drawing everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle1)
    pygame.draw.rect(screen, WHITE, paddle2)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (width//2, 0), (width//2, height))

    # Displaying the score
    text = font.render(str(score_player1), True, WHITE)
    screen.blit(text, (250, 10))
    text = font.render(str(score_player2), True, WHITE)
    screen.blit(text, (380, 10))

    # Updating the display
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()

