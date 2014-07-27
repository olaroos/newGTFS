import sys
import copy
import json

theFile = open('./266_6_BLT_stationIDs', 'r')
raw     = theFile.readlines()
theFile.close()
theFile = open('./266_6_BLT_stationNames', 'r')
rawName    = theFile.readlines()
theFile.close()

ids  = []
name = []

for item in raw:
    ids.append(item.strip('\n'))
for item in rawName:
    name.append(item.strip('\n'))
    
css = []
nestcss = {}
nestcss['position'] = 'absolute'
nestcss['top'] = '247px'
left    = 35
for i in range(0,29):
    nestcss['sid']  = ids[i]
    nestcss['left'] = str(i*left)+'px'
    nestcss['id']   = str(i+1)
    nestcss['name'] = name[i]                    
    css.append(copy.deepcopy(nestcss))

MotherString = ""
case = sys.argv[1]
if (int(case) == 1):

    for i in range(0,29):
        stationid = str(i+1)
        MotherString = MotherString + "<img src='./img/stationDot62.png' class='imgStation6' name='6"+ name[i] +"' style='left:" + str((i)*left) + ";top: 120px; position:absolute; width:22px' id=" + ids[i] + " left=" + str((i)*left) + "px top=120px stationid=" + stationid + " ng-click='getStationInfo($event)' track='6' posTime='' posBuss='' negBuss='' negTime=''>"
    print MotherString

if (int(case) == 2):

    MotherString = "<ul id='track6names'>"
    for i in range(0,15):
        pos = i*2
        MotherString = MotherString + "<li class='imgStation6' id='6" + name[pos] + "'>" + name[pos] + "</li>"
    MotherString = MotherString + "</ul>"

    print MotherString    

    MotherString = "<ul id='track6names2'>"
    for i in range(0,14):
        pos = i*2 + 1
        MotherString = MotherString + "<li class='imgStation6' id='6" + name[pos] + "'>" + name[pos] + "</li>"
    MotherString = MotherString + "</ul>"

    print MotherString
    print "\r\n"

if (int(case) == 3):

    MotherString = "{ "
    for i in range(0,29):
        MotherString = MotherString + "'" + ids[i] + "' : '" + str(i) + "', "
    MotherString = MotherString + " }"

    print MotherString

