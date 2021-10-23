import sys, time, random
import pygame
from pygame.locals import *

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

def print_text(font, x, y, text, color=(0, 0, 0), Center = False):
	imgText = font.render(text, True, color)
	if Center == True:
		screen.blit(imgText, imgText.get_rect(center=(x,y)))
	else:
		screen.blit(imgText, (x,y))

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Keyboard Speed Test")
font1 = pygame.font.SysFont('arial', 24)
font2 = pygame.font.SysFont('arial', 200)

white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)
screen_color = (203, 240, 247)

key_flag = False
correct_answer = 97
seconds = 10.5
score = 0
clock_start = 0
Start = False
game_over = False

while True:
	while Start == False:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		keys = pygame.key.get_pressed()
		if keys[K_ESCAPE]:
			sys.exit()
		if keys[K_RETURN]:
			Start = True
		screen.fill(white)
		print_text(font1, 400, 300, "Press Enter to start...", Center = True)
		pygame.display.update()

	clock_start = time.clock()
	while game_over == False:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN:
				key_flag = True
			elif event.type == KEYUP:
				key_flag = False

		keys = pygame.key.get_pressed()
		if keys[K_ESCAPE]:
			sys.exit()

		current = time.clock() - clock_start
		speed = score * 6
		if seconds - current < 0:
			game_over = True
		elif current <= 10:
			if keys[correct_answer]:
				correct_answer = random.randint(97, 122)
				score += 1

		screen.fill(screen_color)
		print_text(font1, 0, 20, "Try to keep up for 10 seconds...")

		if key_flag:
			print_text(font1, 450, 0, "you are keying...")		
		
		print_text(font1, 0, 80, "Time: " + str(int(seconds - current)))

		print_text(font2, 400, 300, chr(correct_answer - 32), yellow, Center = True)

		pygame.display.update()

	clock_start = time.clock()
	while Start == True and game_over == True:
		screen.fill(white)
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		current = time.clock() - clock_start
		keys = pygame.key.get_pressed()
		if keys[K_ESCAPE]:
			sys.exit()
		if current > 2:
			print_text(font1, 400, 300, "Press Enter to start again...", Center = True)
			if keys[K_RETURN]:
				Start = False
				game_over = False
				score = 0
				seconds = 10.5
		print_text(font1, 400, 200, "Speed: " + str(speed) + " letters/min", Center = True)
		pygame.display.update()