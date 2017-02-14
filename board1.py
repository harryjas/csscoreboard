import pygame, sys, pickle, random
from pygame.locals import *

pygame.init()
size = (1280, 800)			# (1280, 600)screen resolution
screen = pygame.display.set_mode(size, FULLSCREEN)

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
	fullscreen = True
	logs = []
	while True:
		screen.fill((255,255,255))	# background color
		data = readData(slot)
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type is KEYDOWN and event.key == K_x:
				if (pygame.key.get_mods() & pygame.KMOD_ALT) and (pygame.key.get_mods() & pygame.KMOD_CTRL) and (pygame.key.get_mods() & pygame.KMOD_SHIFT):
					for team in data:
						data[team][1]=data[team][2]=0
						dumpData(slot, data)
			if event.type is KEYDOWN and event.key in [ord(x) for x in data.keys()]:
				if pygame.key.get_mods() & pygame.KMOD_ALT:
					data[chr(event.key)][2] += 1 			# Add 1 loss
					logs.append(("Team : %s lost a match. %s" %(data[chr(event.key)][0], random.choice(["Too bad.", "Better luck next time...", "They need to try harder.", "Come on!"])),(255,0,0)))
					if len(logs)==6:
						logs.pop(0)
				if pygame.key.get_mods() & pygame.KMOD_CTRL:
					data[chr(event.key)][1] += 1 			# Add 1 win
					logs.append(("Team : %s won a match! %s" %(data[chr(event.key)][0], random.choice(["Thats good.", "Job well done!", "They rock!", "Smooth."])),(0,255,0)))
					if len(logs)==6:
						logs.pop(0)
			if event.type is KEYDOWN and event.key == K_z:
				if fullscreen:
					pygame.display.set_mode(size)
					fullscreen = False
				else:
					pygame.display.set_mode(size, FULLSCREEN)
					fullscreen = True
			if event.type is KEYDOWN and event.key == K_TAB:
				slot = 1 if slot == 2 else 2
				data = readData(slot)
		displayText("Slot %s" %slot, 20, (0,0,0), (1240,0))
		byWins = sorted(sorted(data.values()), key=lambda x:x[1], reverse=True)		# Ranking teams
		#displayText("P.U.L.o.G.", 40, (255,100,0),(560,10))
		displayText("Counter Strike 1.6 Tournament", 60, (0,0,255), (320, 20))
		displayText("Scoreboard", 50, (255,100,0),(540,70))
		displayText("Rank", 45, (0,0,0), (130,120))
		displayText("Team Name", 45, (0,0,0), (280,120))
		displayText("Wins", 45, (0,0,0), (680,120))
		displayText("Losses", 45, (0,0,0), (830,120))
		displayText("Win %age", 45, (0,0,0), (980,120))
		startY = 180 
		for i in range(len(byWins)):
			displayText("%d" %(i+1), 45, (0,100,0), (160,startY))
			displayText("%s" %(byWins[i][0]), 40, (0,100,100), (300,startY))
			displayText("%d" %(byWins[i][1]), 45, (0,255,0), (700,startY))
			displayText("%d" %(byWins[i][2]), 45, (255,0,0), (860,startY))
			matches = byWins[i][2]+byWins[i][1]
			displayText("%d%%" %((float(byWins[i][1])/(byWins[i][2]+byWins[i][1]))*100 if matches>0 else 0), 45, (0,0,255), (1010,startY))
			startY += 80

		for log in logs[::-1]:
			displayText("%s" %(log[0]), 25, log[1], (160,startY))
			startY+=30
		dumpData(slot, data)
		pygame.display.update()

main()
