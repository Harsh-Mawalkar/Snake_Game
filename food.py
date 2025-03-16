import pygame
import random
from config import *

class Food:
    def __init__(self):
        self.position = (0,0)
        self.spawn_food([])
    
    def spawn_food(self,snake_body):
        while True:
            x = random.randint(0,(GAME_WIDTH // GRID_SIZE)-1)* GRID_SIZE
            y = random.randint(0,(GAME_HEIGHT // GRID_SIZE)-1)* GRID_SIZE
            self.position=(x,y)

            if self.position not in snake_body:
                break

    def draw(self,screen):
        pygame.draw.rect(screen,FOOD_COLOR,(self.position[0],self.position[1],GRID_SIZE,GRID_SIZE))