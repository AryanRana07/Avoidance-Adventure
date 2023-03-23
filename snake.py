import pygame
import random
import sys

pygame.init()

#Screen
SPEED = 10
WIDTH = 800
HEIGHT = 600
RED = (255,0,0)
BLUE = (0,0,255)
BG_COLOR = (0,0,0)

#Player
player_size = 50
player_pos = [WIDTH/2,HEIGHT-2*player_size]

#Enemy
enemy_size = 50
enemy_pos = [random.randint(0,WIDTH-enemy_size),0]

screen = pygame.display.set_mode((WIDTH,HEIGHT))

game_over = False

clock = pygame.time.Clock()