from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import COMET

class Comet (Obstacle):
    Y_POS_COMET = 275
    X_POS_COMET = 3000

    def __init__(self):
        self.image = COMET
        super().__init__(self.image)
        self.rect.y = self.Y_POS_COMET