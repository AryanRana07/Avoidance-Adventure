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

#Game loop
while not game_over:
	
	for event in pygame.event.get():
		
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.KEYDOWN:
			
			x= player_pos[0]
			y= player_pos[1]

			if event.key == pygame.K_LEFT:
				x -= player_size
			elif event.key == pygame.K_RIGHT:
				x += player_size

			player_pos = [x,y]

	screen.fill(BG_COLOR)

#Updating pos of enemy
	if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
		enemy_pos[1] += SPEED

	else:
		enemy_pos[0] = random.randint(0,WIDTH - enemy_size)
		enemy_pos[1] = 0
#Collision
	# if detect_coll(player_pos,enemy_pos):
	# 	game_over = True 
		

	pygame.draw.rect(screen, BLUE, (enemy_pos[0],enemy_pos[1] ,enemy_size ,enemy_size))
	pygame.draw.rect(screen, RED, (player_pos[0],player_pos[1] ,player_size ,player_size))

	clock.tick(30)

	pygame.display.update()
 