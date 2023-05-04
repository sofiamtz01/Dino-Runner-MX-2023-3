from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.birds import Bird

class ObstacleManager:
    def __init__(self):
        self.obstacles = []


    def update(self, game_speed, player):
        if len(self.obstacles) ==0:
            self.obstacles.append(Cactus())          
        for obstacle in self.obstacles:
            if obstacle.rect.x < -obstacle.rect.width:
                self.obstacles.remove(obstacle)
            obstacle.update(game_speed, player)

        if len(self.obstacles) ==0:
            self.obstacles.append(Bird())          
        for obstacle in self.obstacles:
            if obstacle.rect.x < -obstacle.rect.width:
                self.obstacles.remove(obstacle)
            obstacle.update(game_speed, player)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []
