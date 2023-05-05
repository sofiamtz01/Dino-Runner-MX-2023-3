import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, CLOUD
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.components import text_utils


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 5
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.x_pos_cloud = 600
        self.y_pos_cloud = 160
        self.obstaclemanager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.points = 0
        self.running = True
        self.death_count = 0 

        self.high_score = 0
    

    def execute(self):
        while self.running:
            if not self.playing:
                self.show_menu()

    def show_menu(self):
        self.running = True
        white_color =(255, 255, 255)
        self.screen.fill(white_color)

        self.print_menu_elements()
        pygame.display.update()

        self.handle_key_events_on_menu()

    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.player = False
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                self.run()

    def print_menu_elements(self):
        if self.death_count == 0:
            text, text_rect = text_utils.get_center_message("Press any Key to Start")
            self.screen.blit(text, text_rect)
        if self.death_count > 0:
            text, text_rect = text_utils.get_center_message("Press any Key to Start")
            self.screen.blit(text, text_rect)
        if self.high_score > 0:
            high_score_text, high_score_rect = text_utils.get_center_message("High Score: " + str(self.high_score), height=320)
            self.screen.blit(high_score_text, high_score_rect)
    
    def reset(self):
        self.player = False
        self.game_speed = 20
        self.points = 0
        self.running = True
        self.death_count = 0
        self.player = Dinosaur()
        self.obstaclemanager.reset_obstacles()
        self.power_up_manager.reset_Power()
        self.lives = 3


    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.reset()
        while self.playing:
            self.events()
            self.update()
            self.draw()


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        if self.points > self.high_score:
            self.high_score = self.points
        self.points += 1

        user_input = pygame.key.get_pressed()
        self.player.update(user_input)

        self.obstaclemanager.update(self.game_speed, self.player)
        self.power_up_manager.update(self.game_speed, self.points, self.player)
        if self.player.dino_dead:
            self.playing = False


    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.score()
        self.player.draw(self.screen)
        self.draw_cloud()
        self.obstaclemanager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_cloud(self):
        image_width = CLOUD.get_width()
        self.screen.blit(CLOUD, (self.x_pos_cloud, self.y_pos_cloud))
        if self.x_pos_cloud <= -image_width:
            self.screen.blit(CLOUD, (image_width + self.x_pos_cloud, self.y_pos_cloud))
            self.x_pos_cloud = 2000
        self.x_pos_cloud -= self.game_speed

    def score(self):
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed +=1
        
        text, text_rect = text_utils.get_score_element(self.points)
        self.screen.blit(text, text_rect)