import sys
import copy
import json

theFile = open('./266_2_BLT_stationIDs', 'r')
raw     = theFile.readlines()
theFile.close()
theFile = open('./266_2_BLT_stationNames', 'r')
rawName    = theFile.readlines()
theFile.close()
theFile = open('./266_2_BLT_stationNames_nogap', 'r')
rawNameNoGap    = theFile.readlines()
theFile.close()

ids  = []
name = []
namenogap = []

for item in raw:
    ids.append(item.strip('\n'))
for item in rawName:
    name.append(item.strip('\n'))
for item in rawNameNoGap:
    namenogap.append(item.strip('\n')) 
    
css = []
nestcss = {}
nestcss['position'] = 'absolute'
nestcss['top'] = '247px'
left    = 35
for i in range(0,34):
    nestcss['sid']  = ids[i]
    nestcss['left'] = str(i*left)+'px'
    nestcss['id']   = str(i+1)
    nestcss['name'] = name[i]                    
    css.append(copy.deepcopy(nestcss))

MotherString = ""
case = sys.argv[1]

if (int(case) == 1):

    for i in range(0,34):
        stationid = str(i+1)
        MotherString = MotherString + "<img src='./img/stationDot22.png' class='imgStation2 hoverClass' name='2"+ namenogap[i] +"' style='left:" + str((i)*left) + ";top: 120px; position:absolute;' id=" + ids[i] + " left=" + str((i)*left) + "px top=120px stationid=" + stationid + " ng-click='getStationInfo($event)' track='2' posTime='' posBuss='' negBuss='' negTime=''>"
    print MotherString

if (int(case) == 2):

    MotherString = "<ul id='track2names'>"
    for i in range(0,17):
        pos = i*2
        MotherString = MotherString + "<li class='imgStation2' id='2" + namenogap[pos] + "'>" + name[pos] + "</li>"
    MotherString = MotherString + "</ul>"

    print MotherString
    print "\r\n"

    MotherString = "<ul id='track2names2'>"
    for i in range(0,17):
        pos = i*2 + 1
        MotherString = MotherString + "<li class='imgStation2' id='2" + namenogap[pos] + "'>" + name[pos] + "</li>"
    MotherString = MotherString + "</ul>"

    print MotherString

if (int(case) == 3):

    MotherString = "{ "
    for i in range(0,34):
        MotherString = MotherString + "'" + ids[i] + "' : '" + str(i) + "', "
    MotherString = MotherString + " }"

    print MotherString

if (int(case) == 4):

    MotherString = ""
    for i in range(0,34):
        stationid = str(i+1)
        MotherString = MotherString + "<div  class='imgStation2' name='1"+ namenogap[i] +"' style='left:" + str((i)*left) + ";top: 120px; position:absolute;' id=" + ids[i] + " left=" + str((i)*left) + "px top=120px stationid=" + stationid + " ng-click='getStationInfo($event)' track='2' posTime='' posBuss='' negBuss='' negTime=''> </div> "
    print MotherString




