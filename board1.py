import pygame, sys
from pygame.locals import *

pygame.init()

def readData(slot):				# slot is the time slot ;)
	dataFile = open(["team_data1.txt", "team_data2.txt",][slot-1], "r")
	data = []
	for team in dataFile.readlines():
		temp = team.split(',')
		data.append([temp[0], int(temp[1]), int(temp[1]), temp[-1][:-1]])
	dataFile.close()
	return data

def main():
	size = (1280, 800)			# (1280, 600)screen resolution
	slot = 1 					# slot number
	screen = pygame.display.set_mode(size)
	while True:
		screen.fill((255,255,255))	# background color
		data = readData(slot)
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type is KEYDOWN and event.key == K_w:
				pygame.display.set_mode(size)
			if event.type is KEYDOWN and event.key == K_f:
				pygame.display.set_mode(size, FULLSCREEN)
			if event.type is KEYDOWN and event.key == K_TAB:
				slot = 1 if slot == 2 else 2
				print data
		myfont = pygame.font.SysFont("monospace", 70)

		# render text
		label = myfont.render("Some text!", 1, (255,255,0))
		screen.blit(label, (100, 100))
		pygame.display.update()
main()