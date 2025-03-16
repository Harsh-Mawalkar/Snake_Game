import pygame
from config import *

class Snake:
    def __init__(self):
        self.body = [(GRID_SIZE * 5, GRID_SIZE * 5)]
        self.direction = (GRID_SIZE, 0)
        self.growing = False  
        self.score = 0

    def move(self, food_pos):
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])

        self.body.insert(0, new_head)  # Add new head

        # ✅ Check if food is eaten
        if new_head == food_pos:
            self.growing = True  # ✅ Don't remove the last part
            self.score +=10
            return True  
        else:
            self.growing = False
            self.body.pop()  # Remove last segment only if not growing
            return False  

    def collusion_check(self):
        head_x, head_y = self.body[0]
        if head_x < 0 or head_x >= GAME_WIDTH or head_y < 0 or head_y >= GAME_HEIGHT:
            return True
        if self.body[0] in self.body[1:]:  # Self-collision
            return True
        return False

    def change_direction(self, key):
        if key == pygame.K_UP and self.direction != (0, GRID_SIZE):
            self.direction = (0, -GRID_SIZE)
        elif key == pygame.K_DOWN and self.direction != (0, -GRID_SIZE):
            self.direction = (0, GRID_SIZE)
        elif key == pygame.K_LEFT and self.direction != (GRID_SIZE, 0):
            self.direction = (-GRID_SIZE, 0)
        elif key == pygame.K_RIGHT and self.direction != (-GRID_SIZE, 0):
            self.direction = (GRID_SIZE, 0)

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, SNAKE_COLOR, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))
