import asyncio
import sys, pygame
from config import *
from snake import Snake
from food import Food

pygame.init()
screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

font = pygame.font.Font(None, 36)

snake = Snake()
food = Food()

def draw_score():
    score_text = font.render(f"Score: {snake.score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

def show_game_over():
    font = pygame.font.Font(None, 36)
    text = font.render("Game Over! Press any key to restart", True, (255, 0, 0))
    text_rect = text.get_rect(center=(GAME_WIDTH // 2, GAME_HEIGHT // 2))
    screen.blit(text, text_rect)

async def main():
    global snake, food
    running = True
    game_over = False

    while running:
        screen.fill(BACKGROUND_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if game_over:
                if event.type == pygame.KEYDOWN:
                    snake = Snake()
                    food = Food()
                    game_over = False
                continue

            if event.type == pygame.KEYDOWN:
                snake.change_direction(event.key)

        if not game_over:
            if snake.move(food.position):
                food.spawn_food(snake.body)

            snake.draw(screen)
            food.draw(screen)
            draw_score()

            if snake.collusion_check():
                game_over = True
            
        if game_over:
            show_game_over()

        pygame.display.flip()
        clock.tick(SPEED)

        # ✅ Required for pygbag to work in browser
        await asyncio.sleep(0)

asyncio.run(main())  # ✅ Runs the game asynchronously
