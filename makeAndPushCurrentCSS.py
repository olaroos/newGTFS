import copy
import json

motherCSS = {}

# Calculate TRACK 1! css properties -------------------------------------------

theFile = open('266_1_BLT/266_1_BLT_stationIDs', 'r')
raw     = theFile.readlines()
theFile.close()
theFile = open('266_1_BLT/266_1_BLT_stationNames_nogap', 'r')
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
for i in range(0,30):
    nestcss['sid']  = ids[i]
    nestcss['left'] = str(i*left)+'px'
    nestcss['id']   = str(i+1)
    nestcss['name'] = name[i]                    
    css.append(copy.deepcopy(nestcss))

motherCSS[1] = copy.deepcopy(css)

# Calculate TRACK 2! css properties -------------------------------------------

theFile = open('266_2_BLT/266_2_BLT_stationIDs', 'r')
raw     = theFile.readlines()
theFile.close()
theFile = open('266_2_BLT/266_2_BLT_stationNames_nogap', 'r')
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
for i in range(0,34):
    nestcss['sid']  = ids[i]
    nestcss['left'] = str(i*left)+'px'
    nestcss['id']   = str(i+1)
    nestcss['name'] = name[i]                    
    css.append(copy.deepcopy(nestcss))

motherCSS[2] = copy.deepcopy(css)

# Calculate TRACK 3! css properties -------------------------------------------

theFile = open('266_3_BLT/266_3_BLT_stationIDs', 'r')
raw     = theFile.readlines()
theFile.close()
theFile = open('266_3_BLT/266_3_BLT_stationNames_nogap', 'r')
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
for i in range(0,30):
    nestcss['sid']  = ids[i]
    nestcss['left'] = str(i*left)+'px'
    nestcss['id']   = str(i+1)
    nestcss['name'] = name[i]                    
    css.append(copy.deepcopy(nestcss))

motherCSS[3] = copy.deepcopy(css)

# Calculate TRACK 4! css properties -------------------------------------------

theFile = open('266_4_BLT/266_4_BLT_stationIDs', 'r')
raw     = theFile.readlines()
theFile.close()
theFile = open('266_4_BLT/266_4_BLT_stationNames_nogap', 'r')
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
for i in range(0,32):
    nestcss['sid']  = ids[i]
    nestcss['left'] = str(i*left)+'px'
    nestcss['id']   = str(i+1)
    nestcss['name'] = name[i]                    
    css.append(copy.deepcopy(nestcss))

motherCSS[4] = copy.deepcopy(css)

# Calculate TRACK 5! css properties -------------------------------------------

theFile = open('266_5_BLT/266_5_BLT_stationIDs', 'r')
raw     = theFile.readlines()
theFile.close()
theFile = open('266_5_BLT/266_5_BLT_stationNames_nogap', 'r')
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
for i in range(0,27):
    nestcss['sid']  = ids[i]
    nestcss['left'] = str(i*left)+'px'
    nestcss['id']   = str(i+1)
    nestcss['name'] = name[i]                    
    css.append(copy.deepcopy(nestcss))

motherCSS[5] = copy.deepcopy(css)


# Calculate TRACK 6! css properties -------------------------------------------

theFile = open('266_6_BLT/266_6_BLT_stationIDs', 'r')
raw     = theFile.readlines()
theFile.close()
theFile = open('266_6_BLT/266_6_BLT_stationNames_nogap', 'r')
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

motherCSS[6] = copy.deepcopy(css)


# ------------- Make SQL-calls ---------------

output = json.dumps(motherCSS, ensure_ascii=True)
# push to mysql

import MySQLdb

DB              = 'VBUSS'
DB_HOST         = '127.0.0.1'
DB_USER         = 'root'
DB_PASSWORD     = ''
conn = MySQLdb.Connection(db=DB, host=DB_HOST, user=DB_USER,passwd=DB_PASSWORD)
c = conn.cursor()

c.execute("set autocommit = 1")
c.execute("""truncate table css""")
c.execute("""INSERT INTO css (jsonFile) VALUES (%s);""", (output,))
conn.close()

DB              = 'VBUSS'
DB_HOST         = '188.226.223.188'
DB_USER         = 'root'
DB_PASSWORD     = 'lemmeltagetforti'
conn = MySQLdb.Connection(db=DB, host=DB_HOST, user=DB_USER,passwd=DB_PASSWORD)
c = conn.cursor()

c.execute("set autocommit = 1")
c.execute("""truncate table css""")
c.execute("""INSERT INTO css (jsonFile) VALUES (%s);""", (output,))
conn.close()

