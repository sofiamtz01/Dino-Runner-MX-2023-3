import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS
class Cactus(Obstacle):
    Y_POS_CACTUS = 325
    X_POS_CACTUS = 2000

    def __init__(self):
        self.image = random.choice(SMALL_CACTUS + LARGE_CACTUS)
        super().__init__(self.image)
        self.rect.y = self.Y_POS_CACTUS
        self.rect.x = self.X_POS_CACTUS  
