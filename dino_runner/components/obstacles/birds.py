from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class Bird (Obstacle):
    Y_POS_BIRD = 125
    X_POS_BIRD  = 3000

    def __init__(self):
        self.image = BIRD[0]
        super().__init__(self.image)
        self.rect.y = self.Y_POS_BIRD