#!/bin/bash
rm 266_6_BLT_trips_withoutblankspace
cat 266_6_BLT_trips | awk 'BEGIN {FS=",";} { print $0 }' | tr -d '[:blank:]' >> 266_6_BLT_trips_withoutblankspace
mv 266_6_BLT_trips_withoutblankspace 266_6_BLT_trips

