import pygame
import random

# Step 1: Initialize pygame and set up the display
pygame.init()

# Screen dimensions
width, height = 800, 600

# Colors
bg_color = (34, 40, 49)  # Dark background
snake_color = (57, 255, 20)  # Bright green snake
food_color = (255, 69, 58)  # Bright red food
text_color = (248, 248, 255)  # Light text color
game_over_color = (255, 87, 51)  # Orange for game over text

# Initialize game screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Clock to control game speed
clock = pygame.time.Clock()

# Snake block size and speed
block_size = 20
snake_speed = 15

# Fonts for score and messages
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


# Function to display score
def show_score(score):
    value = score_font.render(f"Score: {score}", True, text_color)
    screen.blit(value, [10, 10])


# Function to display the snake
def draw_snake(block_size, snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, snake_color,
                         [block[0], block[1], block_size, block_size])


# Function to display messages
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])


# Main game loop
def gameLoop():
    # Step 2: Initialize variables
    game_over = False
    game_close = False

    x1, y1 = width // 2, height // 2
    x1_change, y1_change = 0, 0

    snake_list = []
    length_of_snake = 1

    # Generate initial food position
    foodx = round(random.randrange(0, width - block_size) / 20.0) * 20.0
    foody = round(random.randrange(0, height - block_size) / 20.0) * 20.0

    while not game_over:
        while game_close:
            screen.fill(bg_color)
            message(
                "Game Over! Womp Womp. Press Q to quit or C to play again.",
                game_over_color)
            show_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # Step 3: Handle events (e.g., arrow key presses)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = block_size
                    x1_change = 0

        # Step 4: Update snake position
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change

        # Step 5: Draw screen, food, and snake
        screen.fill(bg_color)
        pygame.draw.rect(screen, food_color,
                         [foodx, foody, block_size, block_size])

        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check if the snake collides with itself
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(block_size, snake_list)
        show_score(length_of_snake - 1)
        pygame.display.update()

        # Step 6: Check for food collision
        if x1 == foodx and y1 == foody:
            foodx = round(
                random.randrange(0, width - block_size) / 20.0) * 20.0
            foody = round(
                random.randrange(0, height - block_size) / 20.0) * 20.0
            length_of_snake += 1

        clock.tick(snake_speed)

    # Quit pygame
    pygame.quit()
    quit()


# Start the game
gameLoop()
