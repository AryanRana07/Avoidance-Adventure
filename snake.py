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

def detect_coll(player_pos, enemy_pos):
	p_x = player_pos[0]
	p_y = player_pos[1]

	e_x = player_pos[0]
	e_y = player_pos[1]

	if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x + enemy_size)):
		if(e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y + enemy_size)):
			return True
	return False