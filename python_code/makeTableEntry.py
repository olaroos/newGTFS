import sys
import codecs
import json
import datetime
import time
import copy
import MySQLdb

print "\r\n"

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
    print "Found the earliest departure leaving at " + dataBase[saveKey][0][3] + ' from ' + dataBase[saveKey][0][5]
    return saveKey

def findMatch(keyForItem, matchThisItem, condition):
    maximum = float("inf")
    minimum = float("-inf")
    arriveTimeStamp = getTimeStamp(matchThisItem[-1][4])
    
    for key2, item2 in serviceB.iteritems():
        conditionEndMatchStart   = ( matchThisItem[-1][5] == item2[0][5] )
        
        if ( conditionEndMatchStart):
            departTimeStamp = getTimeStamp(item2[0][3])
            today = time.strftime("%Y-%m-%d", time.localtime())
            diff  = departTimeStamp - arriveTimeStamp             
            if ( (arriveTimeStamp <= departTimeStamp) and (departTimeStamp < maximum) ):
                maximum     = departTimeStamp
                savediff    = departTimeStamp - arriveTimeStamp 
                saveKey2    = key2

    if (condition):
        upperBound        = 3600
    else: 
        upperBound        = float("inf")

    if('saveKey2' in locals()):
        if (savediff < upperBound):
            # print 'matched station id ' + matchThisItem[-1][5] + ' arriving at ' + matchThisItem[-2][4] + ' leaving at ' + serviceB[saveKey2][0][3]
            # print diff
            return saveKey2
        else:
            print 'the wait for this buss at station id ' + matchThisItem[-1][5] + ' arriving at ' + matchThisItem[-2][4] + ' was more than ' + str(upperBound) + "\r\n"
    else:
        print 'did not find a match for station id ' + matchThisItem[-1][5] + ' arriving at ' + matchThisItem[-2][4] + "\r\n"
    
def checkRoutes(bussesArray):
    count = 1
    for item in bussesArray:
        print "Buss number " + str(count) + " :"
        for subItem in item:
            print subItem[0][3] + " " + subItem[-1][4]
        count += 1


# filename        = 'parsed/266_5_BLT_trips_stops_service_id_643_trunced'
# service_id      = '643'
filename        = sys.argv[1]
service_id      = sys.argv[2]
track           = sys.argv[3]
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
     
GCounter    = 0
earliestKey = findEarliestDep(serviceB)
condition   = True


while(loop):
    if (GCounter < 5):
        condition = True
    else:
        condition = False

    matchedKey  = findMatch(earliestKey, serviceB[earliestKey], condition)
    busses[-1].append(copy.deepcopy( serviceB[str(earliestKey)] ))
    del serviceB[earliestKey]    

    if ( matchedKey != None ):
        earliestKey = matchedKey
    else:
        GCounter += 1
        if (len(serviceB) > 1):
            earliestKey = findEarliestDep(serviceB)
            busses.append([])
        else:
            loop = False
            print "\r\n"

counter = 0
for item in busses:
    concatBusses.append([])
    for subItem in item:
        for subSubItem in subItem:
            concatBusses[counter].append(subSubItem)
    counter += 1    
print service_id
print counter

bussesJson  = json.dumps(concatBusses, ensure_ascii=True)

DB              = 'VBUSS'
DB_HOST         = '127.0.0.1'
DB_USER         = 'root'
DB_PASSWORD     = 'newpassword'

conn        = MySQLdb.Connection(db=DB, host=DB_HOST, user=DB_USER,passwd=DB_PASSWORD)
c           = conn.cursor()

c.execute("set autocommit = 1")

c.execute("""INSERT INTO VL (jsonFile, id_num, service_id) VALUES (%s, %s, %s);""", (bussesJson, track, service_id))
conn.close()

# DB              = 'VBUSS'
# DB_HOST         = '188.226.223.188'
# DB_USER         = 'root'
# DB_PASSWORD     = 'lemmeltagetforti'

# conn        = MySQLdb.Connection(db=DB, host=DB_HOST, user=DB_USER,passwd=DB_PASSWORD)
# c           = conn.cursor()

# c.execute("set autocommit = 1")

# c.execute("""INSERT INTO VL (jsonFile, id_num, service_id) VALUES (%s, 6, %s);""", (bussesJson, service_id))
# conn.close()
