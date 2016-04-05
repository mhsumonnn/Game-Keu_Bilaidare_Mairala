#------------------------------------------------------------------#
#           Keu Bilaitare Mairala                                  #
#------------------------------------------------------------------#

import pygame
import sys
import time
import random
from pygame.locals import*

pygame.init()

# Time set
FPS = 30
fpsClock = pygame.time.Clock()

# Game Variables
Game_point = 0								# Total game point
cats_count = 100							# To change the number of cats appearing every time

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BB3455 = (187, 52, 85)
TURQUOISE = (26, 188, 156)
ASPHALT = (44, 62, 80)

# Sounds
pygame.mixer.music.load("sound/sound1.ogg")
pygame.mixer.music.play(-1, 0)
cat_scream = pygame.mixer.Sound("sound/sound2.ogg")
slap = pygame.mixer.Sound("sound/sound3.ogg")
	
# Window Initialize           
DIS = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Keu Bilaidare Mairala! 2.2.0")

# Set Cursor
pygame.mouse.set_cursor(*pygame.cursors.diamond)

# Load Font
font1 = pygame.font.Font("fonts/Origicide.ttf", 24)
font2 = pygame.font.Font("fonts/Big_Campus_Bold.ttf", 48)
font3 = pygame.font.Font("fonts/BebasNeue.ttf", 24)
font4 = pygame.font.Font("fonts/BebasNeue.ttf", 16)

######################################################################################
#    Pygame Action Start Screen ######################################################
######################################################################################
	
# Images------------------------------------------------------------------------------
logo = pygame.image.load("graphics/logo.png")
title_name = pygame.image.load("graphics/title.png")
title_name_blink = 0

cat = pygame.image.load("graphics/bilai.png")
cat_x = 350
cat_y = 480
cat_x_const = -1
def move_cat():
	global cat_x_i
	global cat_y, cat_x, cat_x_const
	if cat_y >= 250:
		cat_y -= 10
	if cat_y <= 250:
		cat_x += 2*cat_x_const
		if cat_x==300 or cat_x==400:
			cat_x_const *= -1

# Credit text --------------------------------------------------------------------------------

gd1 = font3.render("Mahmudul Hasan Sumon", 1, ASPHALT)
gd2 = font4.render("Graphics, Sprites and Layout", 1, ASPHALT)
gd3 = font3.render("Mrinmoy Biswas Akash", 1, ASPHALT)
gd4 = font4.render("Programming and Development", 1, ASPHALT)
start_game = font1.render("CLICK YOUR MOUSE", 1, WHITE)

def show_credits():
	DIS.blit(gd3, (20, 300))
	DIS.blit(gd4, (20, 325))
	DIS.blit(gd1, (20, 350))
	DIS.blit(gd2, (20, 375))

#---------------------------------------------------------------------------------------------

while True:
	DIS.fill(TURQUOISE)
	DIS.blit(cat, (cat_x, cat_y))
	if title_name_blink > 50:
		show_credits()
	if title_name_blink%3!=0:
		DIS.blit(start_game, (370, 100))
	move_cat()
	
	DIS.blit(title_name, (20, 20))
	title_name_blink += 1

	flag = False
	
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
		elif event.type==MOUSEBUTTONUP:
			flag = True
	
	if(flag):
		break
	pygame.display.update() 
	fpsClock.tick(FPS)

######################################################################################
#    HOW TO PLAY #####################################################################
######################################################################################

DIS.fill( (95, 207, 128) )
hw_to1 = font3.render("Shoot the cat with your mouse", 1, WHITE)
hw_to2 = font3.render("to gain point", 1, WHITE)
DIS.blit(hw_to1, (200, 200))
DIS.blit(hw_to2, (270, 230))
pygame.display.update()
fpsClock.tick(0.2)

######################################################################################
#    Pygame Action Game Play #########################################################
######################################################################################

# Images -----------------------------------------------------------------------------
bg = pygame.image.load("graphics/bg.jpg")
spr1 = pygame.image.load("graphics/spr1.png")
spr2 = pygame.image.load("graphics/spr2.png")
spr3 = pygame.image.load("graphics/spr3.png")
spr4 = pygame.transform.flip(spr3, True, False)
spr_hit = pygame.image.load("graphics/spr_hit.png")


hitText = pygame.image.load("graphics/hit.png")

clouds=[]
for i in xrange(1, 8):
	clouds.append(pygame.image.load("graphics/cloud"+str(i)+".png"))

hit_flag = False
spr_xo, spr_yo = (0, 0)

def draw_background():
	DIS.blit(bg, (0, 0))
	show_score = font1.render('SCORE: '+str(Game_point), 1, WHITE)
	DIS.blit(show_score, (510, 2))
	move_clouds()

cloud_const = []
for i in xrange(1, 8):
	cloud_const.append(i*10)
	
def move_clouds():
	global cloud_const
	for i in xrange(1, 7):
		DIS.blit(clouds[i], (-250 + cloud_const[i], 2+i*5))
		cloud_const[i] = (cloud_const[i] + i - 3) % 720
	

while True:
	cats_count -= 1
	
	spr_x = random.randint(40, 600)
	spr_y = random.randint(100, 420)
	
	if hit_flag:
		DIS.blit(spr_hit, (spr_xo, spr_yo))
		pygame.display.update()
		fpsClock.tick(FPS/2)
		hit_flag = False
	
	draw_background()
	DIS.blit(spr3, (spr_x, spr_y))
	pygame.display.update() 
	fpsClock.tick(FPS/2)
	draw_background()
	DIS.blit(spr4, (spr_x, spr_y))
	pygame.display.update()
	fpsClock.tick(FPS/2) 
	draw_background()
	DIS.blit(spr3, (spr_x, spr_y))
	
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
		elif event.type==MOUSEBUTTONUP:
			mouse_x, mouse_y = event.pos
			if mouse_x>=spr_xo and mouse_x<=spr_xo+53:
				if mouse_y>=spr_yo and mouse_y<=spr_yo+100:
					slap.play()
					hit_flag = True
					Game_point += 1
					if Game_point%5==0:
						cat_scream.play()
					if spr_x<320:
						DIS.blit(hitText, (spr_x+80, spr_y-20))
					else:
						DIS.blit(hitText, (spr_x-180, spr_y-20))
	
	
	spr_xo, spr_yo = spr_x, spr_y
	
	if cats_count==0:
		break
	
	pygame.display.update() 
	fpsClock.tick( FPS / 15 )


######################################################################################
#    Pygame Action Finishing #########################################################
######################################################################################

Finish_color = [(42, 221, 232), (255, 144, 118), (215, 224, 34)]
i=0


while True:
	DIS.fill((44, 62, 80))
	finishing_score = font2.render("YOU SCORED", -1, Finish_color[i%3])
	score_point = font2.render(str(Game_point/10) + str(Game_point%10), 1, Finish_color[i%3])
	
	DIS.blit(finishing_score, (120, 160))
	DIS.blit(score_point, (275, 250))
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
		
	i += 1
	pygame.display.update()
	fpsClock.tick( FPS/4 )
