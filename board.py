import pygame, sys, pickle, random
from pygame.locals import *

pygame.init()
size = (1280, 800)			# (1280, 600)screen resolution
screen = pygame.display.set_mode(size, FULLSCREEN)
logo=pygame.transform.scale(pygame.image.load("logo.png"), (150,150))
def readData(slot):				# slot is the time slot ;)
	dataFile = open(["team_data1.dat", "team_data2.dat",][slot-1], "r")
	data = pickle.load(dataFile)
	dataFile.close()
	return data

def displayText(text, size, color, position, myfont = ""):
	#myfont = pygame.font.Font("neuropolxrg.ttf", size-15)
	if myfont == "":
		myfont = pygame.font.SysFont("monospace", size)
	else:
		myfont = pygame.font.Font(myfont, size-15)
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
	col = 0
	change = 10
	while True:
		col += change
		if col >= 240 or col<=0:
			change *= -1

		screen.fill((255,255,255))	# background color
		data = readData(slot)
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type is KEYDOWN and event.key == K_x:
				if (pygame.key.get_mods() & pygame.KMOD_ALT) and (pygame.key.get_mods() & pygame.KMOD_CTRL) and (pygame.key.get_mods() & pygame.KMOD_SHIFT):
					logs = []
					for team in data:
						data[team][1]=data[team][2]=0
						dumpData(slot, data)
			if event.type is KEYDOWN and event.key in [ord(x) for x in data.keys()]:
				if pygame.key.get_mods() & pygame.KMOD_ALT:
					data[chr(event.key)][2] += 1 			# Add 1 loss
					logs.append(("%s lost a match. %s" %(data[chr(event.key)][0], random.choice(["Too bad.", "Better luck next time...", "They need to try harder.", "Come on!", "This is not gonna work.", ])),(255,0,0)))
					if len(logs)==6:
						logs.pop(0)
				if pygame.key.get_mods() & pygame.KMOD_CTRL:
					data[chr(event.key)][1] += 1 			# Add 1 win
					logs.append(("%s won a match! %s" %(data[chr(event.key)][0], random.choice(["Thats good.", "Job well done!", "They rock!", "Smooth.", "Thats the spirit!", "They are killing it!", "Enemies beware!",])),(0,255,0)))
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
				logs = []
		displayText("Slot %s" %slot, 20, (0,0,0), (1240,0))
		byWins = sorted(sorted(data.values()), key=lambda x:x[1], reverse=True)		# Ranking teams
		#displayText("P.U.L.o.G.", 40, (255,100,0),(560,10))
		displayText("Counter Strike 1.6 Tournament", 60, (col,0,255-col), (250, 20),"neuropolxrg.ttf")
		displayText("Scoreboard", 50, (col,100,0),(500,70),"neuropolxrg.ttf")
		displayText("Rank", 45, (0,0,0), (100,120))
		displayText("Team Name", 45, (0,0,0), (250,120))
		displayText("Code", 45, (0,0,0), (580,120))
		displayText("Wins", 45, (0,0,0), (710,120))
		displayText("Losses", 45, (0,0,0), (860,120))
		displayText("Win %age", 45, (0,0,0), (1010,120))
		startY = 180 
		for i in range(len(byWins)):
			code = ''
			for key, value in data.items():
				if value[0] == byWins[i][0]:
					code = key
			displayText("%d" %(i+1), 50, (0,100,0), (120,startY), "digital-7.ttf")
			displayText("%s" %(byWins[i][0]), 40, (0,100,100), (280,startY))
			displayText("#%s" %(code), 35, (0,0,0), (600,startY))
			displayText("%d" %(byWins[i][1]), 50, (0,255,0), (740,startY), "digital-7.ttf")
			displayText("%d" %(byWins[i][2]), 50, (255,0,0), (900,startY), "digital-7.ttf")
			matches = byWins[i][2]+byWins[i][1]
			displayText("%d%%" %((float(byWins[i][1])/(byWins[i][2]+byWins[i][1]))*100 if matches>0 else 0), 50, (0,0,255), (1050,startY), "digital-7.ttf")
			startY += 80

		for log in logs[::-1]:
			displayText("%s" %(log[0]), 25, log[1], (160,startY))
			startY+=26
		if logs:
			displayText("Recent", 40, (0,0,0), (20,680))
			displayText("Events", 40, (0,0,0), (20,710))
		displayText("Powered By ", 30, (0,0,0), (750,700))
		displayText("Kill 'em ", 50, (0,col,0), (1110,640), "neuropolxrg.ttf")
		displayText("All!", 60, (0,0,col), (1130,680), "neuropolxrg.ttf")
		screen.blit(logo, (900,630))
		dumpData(slot, data)
		pygame.display.update()

main()
