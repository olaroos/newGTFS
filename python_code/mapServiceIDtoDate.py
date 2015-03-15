import sys
import sys
import json
import copy

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
		if (len(item) < 7):
			outputDict[item] = []
			saveItem        = item
		else:
			outputDict[saveItem].append(item)	

	return outputDict

track = sys.argv[1]
arrayB = {}
arrayC = {}
nonraw = makeList('dumpPy/266_'+track+'_BLT_service_id_with_dates')
arrayA = makeArray(nonraw)
nonraw = makeList('dumpPy/266_'+track+'_BLT_service_id_matchtimes')
matchNames = makeArray(nonraw)

for item in arrayA:
	for subItem in arrayA[item]:
		if subItem in arrayB:
			arrayB[subItem].append(item)			
		else:
			arrayB[subItem] = []
			arrayB[subItem].append(item)			

# remove dates with prefix 2 from arrayB
tempArrayB = copy.deepcopy(arrayB)
for item in arrayB:
	if (item[0] == "2"):
		for idx2 in range(0, len(tempArrayB[item])):
			for idx in range(0, len(tempArrayB["1"+item[1:]])-1):	
				if tempArrayB["1"+item[1:]][idx] == tempArrayB[item][idx2]:
					del tempArrayB["1"+item[1:]][idx]
			# making sure we are not removing unprocessed information
			if len(tempArrayB[item]) > 0:
				del tempArrayB[item][idx2]
			else:
				del tempArrayB[item]

# Remove prefix from keys
tempArrayB2 = {}
for item in tempArrayB:
	tempArrayB2[item[1:]] = tempArrayB[item]
arrayB = tempArrayB2

for item in arrayB:	
	if (len(arrayB[item]) > 1):
		item1 = arrayB[item][0]
		item2 = arrayB[item][1]		
		arrayC[item] = []
		if (len(arrayB[item]) == 3):
			item3 = arrayB[item][2]
			timeItem1 = int(matchNames[item1][0][0:2])
			timeItem2 = int(matchNames[item2][0][0:2])
			timeItem3 = int(matchNames[item3][0][0:2])

			list1 		= {timeItem1 : item1, timeItem2 : item2, timeItem3 : item3}
			list2 		= [timeItem1, timeItem2, timeItem3]			
			list2.sort()
			for i in range(len(list2)):
				arrayC[item].append(list1[list2[i]])
				arrayC[item].append(matchNames[list1[list2[i]]][0])
		else:
			if (int(matchNames[item1][0][0:2]) > int(matchNames[item2][0][0:2])):		
				arrayC[item].append(item2)
				arrayC[item].append(matchNames[item2][0])
				arrayC[item].append(item1)
				arrayC[item].append(matchNames[item1][0])
			else:
				arrayC[item].append(item1)
				arrayC[item].append(matchNames[item1][0])
				arrayC[item].append(item2)
				arrayC[item].append(matchNames[item2][0])
	else:
		arrayC[item] = arrayB[item]
		
# print arrayC
jsonFile = json.dumps(arrayC, ensure_ascii=True)

theFile = open('../266_'+track+'_BLT/dumpPy/266_'+track+'_BLT_service_id_with_datesJSON', 'w')
theFile.write(jsonFile)
theFile.close()
