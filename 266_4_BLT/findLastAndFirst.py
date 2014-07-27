import sys
import codecs
import json
import datetime
import time
import copy
import MySQLdb

def getTimeStamp(hourMinuteSecond):
    HMS   = hourMinuteSecond
    today = time.strftime("%Y-%m-%d", time.localtime())
    if ( hourMinuteSecond[0:2] == "24" ):
        HMS    = "00" + HMS[2:]
        today  = today[:-2] + str(int(today[-2:])+1)

    return time.mktime(datetime.datetime.strptime(today + " " + HMS, "%Y-%m-%d %H:%M:%S").timetuple())

def findEarliestDep(dataBase):
    maximum = float("inf")
    saveKey = ""
    for key, item in dataBase.iteritems():
        if ( len(item[0][3]) < 10 ):
            HMS = item[1][3]
        else:
            HMS = item[0][3]
        if ( maximum > getTimeStamp(HMS) ):
            maximum = getTimeStamp(HMS)
            outputMaximum = HMS
            saveKey = key
#     print "Found the earliest departure leaving at " + dataBase[saveKey][0][3]
    return outputMaximum

def findLatestDep(dataBase):
    minimum = float("-inf")
    saveKey = ""
    for key, item in dataBase.iteritems():
        if ( len(item[0][3]) < 10 ):
            HMS = item[-1][3]
        else:
            HMS = item[-1][3]
        if ( minimum < getTimeStamp(HMS) ):
            minimum = getTimeStamp(HMS)
            outputMinimum = HMS
            saveKey = key
#     print "Found the earliest departure leaving at " + dataBase[saveKey][0][3]
    return outputMinimum    

def findMatch(keyForItem, matchThisItem):
    maximum = float("inf")
    arriveTimeStamp = getTimeStamp(matchThisItem[-1][4])
    
    for key2, item2 in serviceB.iteritems():
        conditionEndMatchStart   = ( matchThisItem[-2][5] == item2[1][5] )
        
        if ( conditionEndMatchStart):
            departTimeStamp = getTimeStamp(item2[0][3])
            today = time.strftime("%Y-%m-%d", time.localtime())
            
            if ( (arriveTimeStamp <= departTimeStamp) and (departTimeStamp < maximum) ):
                maximum     = departTimeStamp
                saveKey2    = key2
    if('saveKey2' in locals()):   
        return saveKey2
    
def checkRoutes(bussesArray):
    count = 1
    for item in bussesArray:
        print "Buss number " + str(count) + " :"
        for subItem in item:
            print subItem[0][3] + " " + subItem[-1][4]
        count += 1

filename        = sys.argv[1]
service_id      = sys.argv[2]
serviceA        = []
serviceB        = {}
busses          = []
busses.append([])

openFile    = codecs.open(filename)
mother      = openFile.readlines()
openFile.close()

# Parse the data to workable structure serviceB
for item in mother:
    if (item[0] != " "):
        temp = []
        serviceA.append(item.split(","))
        del serviceA[-1][-1]
        del serviceA[-1][-1]
        del serviceA[-1][-1]
        del serviceA[-1][-1]

for item in serviceA:
    if (item[2] in serviceB):
        serviceB[item[2]].append(item)
    else:
        serviceB[str(item[2])] = []
        serviceB[item[2]].append(item)

# Find earliest departure and last departure of each service_id
earliestTime    = findEarliestDep(serviceB)
latestTime      = findLatestDep(serviceB)


openFile = codecs.open("dumpPy/266_4_BLT_service_id_matchtimes", "a");
openFile.write(earliestTime+"\n")
openFile.write(latestTime+"\n")
openFile.close()
