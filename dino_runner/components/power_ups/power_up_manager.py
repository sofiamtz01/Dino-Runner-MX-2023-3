import random
from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer

class PowerUpManager:
    def __init__(self):
        self.power_ups =[]

    def update(self, game_speed, points, player):
        if len(self.power_ups) == 0:
            choice = random.choice([0,1])
            if choice == 0:
                self.power_ups.append(Hammer())
            elif choice == 1:
                self.power_ups.append(Shield())
                
        for power_up in self.power_ups:
            if power_up.used or power_up.rect.x < -power_up.rect.width:
                self.power_ups.remove(power_up)
            if power_up.used:
                player.set_power_up(power_up) 
            power_up.update(game_speed, player)


    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def remove_powerup(self, powerup):
        self.power_ups.remove(powerup)

    def reset_Power(self):
        self.power_ups = []