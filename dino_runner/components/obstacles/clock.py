from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import CLOCK

class Clock (Obstacle):
    Y_POS_CLOCK = 275
    X_POS_CLOCK = 3000

    def __init__(self):
        self.image = CLOCK
        super().__init__(self.image)
        self.rect.y = self.Y_POS_CLOCK