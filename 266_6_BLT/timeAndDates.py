import json
import codecs 
import datetime
import time 

# Match service_id with its first and last departures
openFile = codecs.open("dumpPy/266_1_BLT_service_id_matchtimes")
raw 	 = openFile.readlines()
openFile.close()

arrayServiceId = {}
dates = {}

for item in raw:
	if (len(item.strip("\n")) < 8):
		arrayServiceId[item.strip("\n")] = []
		key 			= item.strip("\n")
	else:
		arrayServiceId[key].append(item.strip("\n"))

# Make dictionary with date as key pointing to list with service_id
openFile = codecs.open("dumpPy/266_1_BLT_service_id_with_dates")
raw 	 = openFile.readlines()
openFile.close()



for item in raw:
	if (len(item.strip("\n")) < 8):
		serviceId 	= item.strip("\n")		
	else:
		if (item.strip("\n") in dates):
			dates[item.strip("\n")].append(serviceId)
		else:
			dates[item.strip("\n")] = []
			dates[item.strip("\n")].append(serviceId)

# If one date has two collections of routes, set the earliest collection first
print dates
for item in dates:
	if len(dates[item]) > 1:		
		A = arrayServiceId[dates[item][0]][0]
		B = arrayServiceId[dates[item][1]][0]
		if (A[:1] == str(2)):
			Astamp = time.mktime(datetime.datetime.strptime("2014-01-02 00"+ A[2:], "%Y-%m-%d %H:%M:%S").timetuple())	
		else:
			Astamp = time.mktime(datetime.datetime.strptime("2014-01-01 "+A, "%Y-%m-%d %H:%M:%S").timetuple())
		Bstamp = time.mktime(datetime.datetime.strptime("2014-01-01 "+B, "%Y-%m-%d %H:%M:%S").timetuple())		
		print Bstamp
		AserviceId = dates[item][0]
		BserviceId = dates[item][1]
		del dates[item]
		dates[item] = []
		if Astamp > Bstamp :
			print "Remove and add first depart time"
			dates[item].append(BserviceId)
			dates[item].append(B)
			dates[item].append(AserviceId)
			dates[item].append(A)						
		else:
			print "Remove, switch order and add first depart time"			
			dates[item].append(AserviceId)
			dates[item].append(A)
			dates[item].append(BserviceId)
			dates[item].append(B)

# Write to files
serviceIdJSON 	= json.dumps(arrayServiceId)
datesJSON 		= json.dumps(dates)

openFile = codecs.open("dumpPy/service_id_matchtimesJSON", "w")
openFile.write(serviceIdJSON)
openFile.close()

openFile = codecs.open("dumpPy/266_1_BLT_service_id_with_datesJSON", "w")
openFile.write(datesJSON)
openFile.close()