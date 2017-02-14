import pygame, sys, pickle
from pygame.locals import *

pygame.init()
size = (1280, 800)			# (1280, 600)screen resolution
screen = pygame.display.set_mode(size)

def readData(slot):				# slot is the time slot ;)
	dataFile = open(["team_data1.dat", "team_data2.dat",][slot-1], "r")
	data = pickle.load(dataFile)
	dataFile.close()
	return data

def displayText(text, size, color, position):
	myfont = pygame.font.SysFont("monospace", size)	# render text
	label = myfont.render(text, 1, color)
	screen.blit(label, position)

def dumpData(slot,data):
	dataFile = open(["team_data1.dat", "team_data2.dat",][slot-1], "w")
	pickle.dump(data, dataFile)
	dataFile.close()


def main():
	slot = 1 					# slot number

	while True:
		screen.fill((255,255,255))	# background color
		data = readData(slot)
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type is KEYDOWN and event.key in [ord(x) for x in data.keys()]:
				if pygame.key.get_mods() & pygame.KMOD_ALT:
					data[chr(event.key)][2] += 1 			# Add 1 loss
				if pygame.key.get_mods() & pygame.KMOD_CTRL:
					data[chr(event.key)][1] += 1 			# Add 1 win
				print data[chr(event.key)]
			
			if event.type is KEYDOWN and event.key == K_w:
				pygame.display.set_mode(size)
			if event.type is KEYDOWN and event.key == K_z:
				pygame.display.set_mode(size, FULLSCREEN)
			if event.type is KEYDOWN and event.key == K_TAB:
				slot = 1 if slot == 2 else 2
		displayText("Slot %s" %slot, 20, (0,0,0), (1240,0))
		dumpData(slot, data)
		pygame.display.update()

main()
