import sys
import json
import re
import datetime
import time 

# rawString = "6,1,1,1,1,1,1,1,20150223,20150614"
track = sys.argv[1]
rawString = str(sys.argv[2])
array = re.split(',', rawString)
days = {}

for i in range(1,8):
	days[["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"][i-1]] = int(array[i])

startDate = time.mktime(datetime.datetime.strptime(array[8], "%Y%m%d").timetuple())	
currentDate = startDate
endDate = time.mktime(datetime.datetime.strptime(array[9], "%Y%m%d").timetuple())	

# find out what day the startDate is:
while currentDate <= endDate+24*60*60:
	d = datetime.datetime.fromtimestamp(currentDate)
	if days[time.strftime("%a", d.timetuple())]:
		print "1"+time.strftime("%Y%m%d", d.timetuple());
	currentDate += 24*60*60

# theFile = open('dumpPy/266_'+track+'_calendartxt_parsed', 'w')
# for day in days:
# 	theFile.write("1"+day)
# theFile.close()