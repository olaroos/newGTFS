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
        today  = today[:-2] + str(int(today[-2:]) + 1)


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
            saveKey = key
#     print "Found the earliest departure leaving at " + dataBase[saveKey][0][3]
    return saveKey

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

# filename        = 'parsed/266_6_BLT_trips_stops_service_id_603_trunced'
# service_id      = '603'     
filename        = sys.argv[1]
service_id      = sys.argv[2]
serviceA        = []
serviceB        = {}
loop            = True
busses          = []
concatBusses    = []
counter         = 0


busses.append([])

openFile    = codecs.open(filename)
mother      = openFile.readlines()
openFile.close()

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
     
earliestKey = findEarliestDep(serviceB)

while(loop):
    matchedKey  = findMatch(earliestKey, serviceB[earliestKey])
    busses[-1].append(copy.deepcopy( serviceB[str(earliestKey)] ))
    del serviceB[earliestKey]    

    if ( matchedKey != None ):
        earliestKey = matchedKey
    else:
        if (len(serviceB) > 1):
            earliestKey = findEarliestDep(serviceB)
            busses.append([])
        else:
            loop = False
            print "\r\n"

for item in busses:
    concatBusses.append([])
    for subItem in item:
        for subSubItem in subItem:
            concatBusses[counter].append(subSubItem)
    counter += 1    

print 'service_id: ' + str(service_id) + ' has these many tours: ' + str(counter)
bussesJson  = json.dumps(concatBusses, ensure_ascii=True)

# openFile = codecs.open("outMakeTableEntry", "w")
# openFile.write(bussesJson)
# openFile.close()

DB              = 'VBUSS'
DB_HOST         = '127.0.0.1'
DB_USER         = 'root'
DB_PASSWORD     = ''

conn        = MySQLdb.Connection(db=DB, host=DB_HOST, user=DB_USER,passwd=DB_PASSWORD)
c           = conn.cursor()

c.execute("set autocommit = 1")
c.execute("""INSERT INTO VL (jsonFile, id_num, service_id) VALUES (%s, 6, %s);""", (bussesJson, service_id))
conn.close()

DB              = 'VBUSS'
DB_HOST         = '188.226.223.188'
DB_USER         = 'root'
DB_PASSWORD     = 'lemmeltagetforti'

conn        = MySQLdb.Connection(db=DB, host=DB_HOST, user=DB_USER,passwd=DB_PASSWORD)
c           = conn.cursor()

c.execute("set autocommit = 1")
c.execute("""INSERT INTO VL (jsonFile, id_num, service_id) VALUES (%s, 6, %s);""", (bussesJson, service_id))
conn.close()
