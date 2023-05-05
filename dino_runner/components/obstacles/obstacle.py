import pygame
from dino_runner.utils.constants import SCREEN_WIDTH


class Obstacle():
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.hammer_done = False
        self.clock_slow = False

    def update(self, game_speed, player):
        self.rect.x -= game_speed
        if self.rect.colliderect(player.dino_rect):
            if not player.shield and not player.hammer and not player.clock:
                pygame.time.delay(2000)
                player.dino_dead = True
                player.dead()
            elif player.hammer:
                 self.hammer_done = True
            elif player.clock:
                pygame.time.delay(2000) 

    
    def draw(self, screen):
            screen.blit(self.image, self.rect)