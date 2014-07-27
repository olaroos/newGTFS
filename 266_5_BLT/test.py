import json

def makeList(fileName):
	theFile = open(fileName)
	raw 	= theFile.readlines()
	theFile.close()
	nonraw  = []
	
	for item in raw:
		nonraw.append(item.strip("\r\n"))

	return nonraw