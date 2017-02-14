def main():
	dataFile = open("team_data1.txt", "r")
	data = []
	for team in dataFile.readlines():
		temp = team.split(',')
		data.append([temp[0], int(temp[1]), int(temp[1]), temp[-1][:-1]])
	print data
main()