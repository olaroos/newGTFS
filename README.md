# README for preparing data for vasterasbuss.nu 

GTFS provides the following files, these will have to be collected each time the bus service updates its times. 

Information of latest update found here: 	[https://api.trafiklab.se/samtrafiken/gtfs/feed_info.txt](https://api.trafiklab.se/samtrafiken/gtfs/feed_info.txt)
The file can be found here: 				[https://api.trafiklab.se/samtrafiken/gtfs/sweden.zip?key=CZBdlJBDdqGnAnRAkgukAnQtPxUtaKq1](https://api.trafiklab.se/samtrafiken/gtfs/sweden.zip?key=CZBdlJBDdqGnAnRAkgukAnQtPxUtaKq1)


## Installation 

### 0:


Download the most recent data from https://api.trafiklab.se/samtrafiken/gtfs/sweden.zip?key=CZBdlJBDdqGnAnRAkgukAnQtPxUtaKq1, 
unzip and put content in the newGTFS-folder. 

### 1:

This step is part of figuring out which busses and which company we want to work with. step_1 is hardcoded to give us data
for the VL company. Currently we are using VL so this step can be skipped. 

* bash step_1 1
	This will parse all the current routes specific identifications for the company VL(Västmanlands Läns trafik) to the file "VL"  

* bash step_1 2
	Would give us the identification of a specific buss, at this time hardcoded in the file "step_1"

### 2:
`cd bashBin`
`bash bashBin/extendFileForAwk.sh`

This will extend calendar.txt and calendar_dates.txt so that the last variable will no longer contain a newline/return-character making it eligible for step 4.3

### 3:

`python python_code/clearTables.py`

This will clear the database as the rows are not unique, we need to remove old data

### 4:

Enter each route-specific folder and run: `bash trace_${route_number} x`
	

	* x = 1: 

		This will cut out all data that belongs to the choosen route and company (${route_number} and VL). 
		
	* x = 2:	

		OBS! You may have to update line 157 if endstations has changed on a specific route. 
		This will sort out all trip information for each route_id and move them to the parsed-folder.

	* x = 3: 
	
		OBS! Allow your current ip to make changes on DigitalOcean database.
		This will sort out needed data to folder dumpPy and invoking the following scripts: 

			python makeTableEntry.py
			python findLastAndFirst.py
			python mapServiceIDtoDate.py
				will output dumpPy/266_'+track+'_BLT_service_id_with_datesJSON'
				this data should be put in /vasterasbuss.dev/bin/js/angular/hellspawn.js for the javascript being able to map the current date to which route_id for a specific buss. 
### 5: 

python mapServiceIDtoDate.py is being run in the previous step:

	will output dumpPy/266_'+track+'_BLT_service_id_with_datesJSON'
	this data should be put in /vasterasbuss.dev/bin/js/angular/hellspawn.js for the javascript being able to map the current date to which route_id for a specific buss. 


Known to cause errors:

In each trace_# on line 99 if the names change of the end/start stations between updates of the sourcefile they will not be truncated from the txt file and this will cause the concatenation of routes to break. Creating a ton of shorter routes. 


----------------------------------------------------------------------
Summary of the google standard format with highlighted numbers for awk
----------------------------------------------------------------------

* agency.txt			One or more transit agencies that provide the data in this feed.

* stops.txt			Individual locations where vehicles pick up or drop off passengers.

* routes.txt			Transit routes. A route is a group of trips that are displayed to riders as a single service.	

* trips.txt			Trips for each route. A trip is a sequence of two or more stops that occurs at specific time.	

*  stop_times.txt		Times that a vehicle arrives at and departs from individual stops for each trip.

*  transfers.txt		Rules for making connections at transfer points between routes.

*  feed_info.txt		Additional information about the feed itself, including publisher, version, and expiration information.

*  calendar.txt		Dates for service IDs using a weekly schedule. Specify when service starts and ends, as well as days of the week
					where service is available.

*  calendar_dates.txt	Exceptions for the service IDs defined in the calendar.txt file. If calendar_dates.txt includes ALL dates of 
					service, this file may be specified instead of calendar.txt.

				    A value of 1 indicates that service has been added for the specified date.
					A value of 2 indicates that service has been removed for the specified date.

*  VL:
*  agency_id = 266
*  route_type = # i.e. Buss

*  routes.txt = route_id,agency_id,route_short_name,route_long_name,route_desc,route_type,route_url,route_color,route_text_color

* 	$1 = route_id
* 	$2 = agency_id
* 	$3 = route_short_name
* 	$4 = route_long_name
* 	$5 = route_desc
* 	$6 = route_type
* 	$7 = route_url
* 	$8 = route_color
* 	$9 = route_text_color

*  trips.txt = route_id,service_id,trip_id,trip_headsign,trip_short_name,direction_id,block_id,shape_id

*  	$1 = route_id
* 	$2 = service_id
* 	$3 = trip_id
* 	$4 = trip_headsign
* 	$5 = trip_short_name
* 	$6 = direction_id
* 	$7 = block_id
* 	$8 = shape_id

*  stop_times.txt = trip_id,arrival_time,departure_time,stop_id,stop_sequence,stop_headsign,pickup_type,drop_off_type,shape_dist_traveled

* 	$1 = trip_id
* 	$2 = arrival_time
* 	$3 = departure_time
* 	$4 = stop_id
* 	$5 = stop_sequence
* 	$6 = stop_headsign
* 	$7 = pickup_type
* 	$8 = drop_off_type
* 	$9 = shape_dist_traveled

*  calendar.txt = service_id,monday,tuesday,wednesday,thursday,friday,saturday,sunday,start_date,end_date

* 	$1 	= service_id
* 	$2 	= monday
*  	$3 	= tuesday
*  	$4 	= wednesday
* 	$5 	= thursday
* 	$6 	= friday
* 	$7 	= saturday
* 	$8 	= sunday
* 	$9 	= start_date
* 	$10 = end_date	
