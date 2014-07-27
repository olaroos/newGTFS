import json

track = argv[1]

def makeList(fileName):
	theFile = open(fileName)
	raw 	= theFile.readlines()
	theFile.close()
	nonraw  = []
	
	for item in raw:
		nonraw.append(item.strip("\r\n"))

	return nonraw

def makeArray(listIn):
	outputDict = {}

	for item in listIn:
		if (len(item) < 6):
			outputDict[item] = []
			saveItem        = item
		else:
			outputDict[saveItem].append(item)	

	return outputDict

nonraw 		= makeList('dumpPy/266_'+track'_BLT_service_id_with_dates')
arrayA 		= makeArray(nonraw)

nonraw 		= makeList('dumpPy/266_'+track+'_BLT_service_id_matchtimes')
matchNames 	= makeArray(nonraw)

arrayB = {}

for item in arrayA:
	for subItem in arrayA[item]:
		if subItem in arrayB:
			arrayB[subItem].append(item)			
		else:
			arrayB[subItem] = []
			arrayB[subItem].append(item)			

arrayC = {}

for item in arrayB:	
	if (len(arrayB[item]) > 1):
		item1 = arrayB[item][0]
		item2 = arrayB[item][1]
		arrayC[item] = []
		if (int(matchNames[item1][0][0:2]) > int(matchNames[item2][0][0:2])):			
			arrayC[item].append(item2)
			arrayC[item].append(matchNames[item2][0])
			arrayC[item].append(item1)
			arrayC[item].append(matchNames[item1][0])
	else:
		arrayC[item] = arrayB[item]
		

jsonFile = json.dumps(arrayC, ensure_ascii=True)

theFile = open('dumpPy/266_'+track+'_BLT_service_id_with_datesJSON', 'w')
theFile.write(jsonFile)
theFile.close()
