import pickle

def readData(slot):				# slot is the time slot ;)
	dataFile = open(["team_data1.dat", "team_data2.dat",][slot-1], "r")
	data = pickle.load(dataFile)
	dataFile.close()
	return data

def dumpData(slot, data):
	dataFile = open(["team_data1.dat", "team_data2.dat",][slot-1], "w")
	pickle.dump(data, dataFile)
	dataFile.close()

def main():
	slot = input("Enter slot number (1-2): ")
	data = readData(slot)
	for key in sorted(data):
		print "Current (team %s) name >" %(key), data[key][0]
		newName = raw_input("Enter new name > ")
		if (newName)!="":
			data[key][0] = newName
	dumpData(slot, data)
	return 0
main()
