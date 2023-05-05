import pygame
from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH
FONT_STYLE = "freesansbold.ttf"
black_color = (0,0,0)


def get_score_element(points):
    font = pygame.font.Font(FONT_STYLE)
    text = font.render("points: " + str(points), True, black_color)
    text_rect = text.get_rect()
    text_rect.center =(1000, 50)
    return text, text_rect

def get_center_message(message, width=SCREEN_WIDTH //2, height=SCREEN_HEIGHT //2):
    font = pygame.font.Font(FONT_STYLE)
    text = font.render(message, True, black_color)
    text_rect = text.get_rect()
    text_rect.center =(width, height)
    return text, text_rect

def get_up_message(message, width=SCREEN_WIDTH //2, height=320):
    font = pygame.font.Font(FONT_STYLE)
    text = font.render(message, True, black_color)
    text_rect = text.get_rect()
    text_rect.center =(width, height)
    return text, text_rect