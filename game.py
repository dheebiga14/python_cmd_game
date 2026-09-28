import pygame
import random
import sys

pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake and Ladder - Final")

# Load board image
board = pygame.image.load("bckimg.jpeg")
board = pygame.transform.scale(board, (600, 600))

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 20, 60)
BLUE = (30, 144, 255)

font = pygame.font.SysFont(None, 32)

CELL = 60

# ✅ Standard real-board snakes & ladders
snakes = {
    16: 6, 47: 26, 49: 11, 56: 53, 62: 19,
    64: 60, 87: 24, 93: 73, 95: 75, 98: 78
}

ladders = {
    1: 38, 4: 14, 9: 31, 21: 42,
    28: 84, 36: 44, 51: 67,
    71: 91, 80: 100
}

# Players
p1 = 1
p2 = 1
turn = 1
dice = 0
winner = None

# Convert board position to coordinates
def get_coords(pos):
    pos -= 1
    row = pos // 10
    col = pos % 10

    if row % 2 == 1:
        col = 9 - col

    x = col * CELL + 30
    y = 600 - (row * CELL) - 30
    return x, y

# Move player
def move(pos, dice):
    pos += dice

    # Bounce if exceeds 100
    if pos > 100:
        pos = 100 - (pos - 100)

    # Snake or ladder
    if pos in snakes:
        pos = snakes[pos]
    elif pos in ladders:
        pos = ladders[pos]

    return pos

# Draw players
def draw_players():
    x1, y1 = get_coords(p1)
    x2, y2 = get_coords(p2)

    pygame.draw.circle(screen, RED, (x1 - 10, y1), 10)
    pygame.draw.circle(screen, BLUE, (x2 + 10, y2), 10)

# Game loop
running = True

while running:
    screen.fill(WHITE)

    # Draw board
    screen.blit(board, (0, 50))

    # Draw players
    draw_players()

    # UI text
    info = font.render(f"Player {turn} Turn | Dice: {dice} (Press SPACE)", True, BLACK)
    screen.blit(info, (10, 10))

    if winner:
        win_text = font.render(f"Player {winner} Wins!", True, RED)
        screen.blit(win_text, (200, 10))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not winner:
                dice = random.randint(1, 6)

                if turn == 1:
                    p1 = move(p1, dice)
                    if p1 == 100:
                        winner = 1
                    else:
                        turn = 2
                else:
                    p2 = move(p2, dice)
                    if p2 == 100:
                        winner = 2
                    else:
                        turn = 1
