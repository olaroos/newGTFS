---------------------------------------------
README for preparing data for vasterasbuss.nu 
---------------------------------------------

GTFS provides the following files, these will have to be collected each time the buss service updates its times. 

Information of latest update found here: 	https://api.trafiklab.se/samtrafiken/gtfs/feed_info.txt
The file can be found here: 				https://api.trafiklab.se/samtrafiken/gtfs/sweden.zip?key=CZBdlJBDdqGnAnRAkgukAnQtPxUtaKq1


	agency.txt			One or more transit agencies that provide the data in this feed.
	stops.txt			Individual locations where vehicles pick up or drop off passengers.
	routes.txt			Transit routes. A route is a group of trips that are displayed to riders as a single service.	
	trips.txt			Trips for each route. A trip is a sequence of two or more stops that occurs at specific time.	
	stop_times.txt		Times that a vehicle arrives at and departs from individual stops for each trip.
	transfers.txt		Rules for making connections at transfer points between routes.
	feed_info.txt		Additional information about the feed itself, including publisher, version, and expiration information.
	
	calendar.txt		Dates for service IDs using a weekly schedule. Specify when service starts and ends, as well as days of the week
						where service is available.

	calendar_dates.txt	Exceptions for the service IDs defined in the calendar.txt file. If calendar_dates.txt includes ALL dates of 
						service, this file may be specified instead of calendar.txt.

-------------------------------------------------

Step 0:
-------

Download the most recent data from https://api.trafiklab.se/samtrafiken/gtfs/sweden.zip?key=CZBdlJBDdqGnAnRAkgukAnQtPxUtaKq1, 
unzip and put content in the newGTFS-folder. 

Step 1:
-------

This step is part of figuring out which busses and which company we want to work with. step_1 is hardcoded to give us data
for the VL company. Currently we are using VL so this step can be skipped. 

bash step_1 1
	This will parse all the current routes specific identifications for the company VL(Västmanlands Läns trafik) to the file "VL"  

bash step_1 2
	Would give us the identification of a specific buss, at this time hardcoded in the file "step_1"

Step 2:
-------

Enter each folder and run the following file "trace_${route_number}"

bash trace_${route_number} X
	
X is 1: 
	This will cut out all data that belongs to the choosen route and company (${route_number} and VL). 
	
X is 2: 
	This will sort out all trip information for each route_id and move them to the parsed-folder.

Before executing the following command you need to allow your current ip to make changes
to the database on DigitalOcean as some python scripts will make calls to the database.

X is 3:
	Invoking the following python scripts: 

		python makeTableEntry.py
		python findLastAndFirst.py
		python mapServiceIDtoDate.py
			will output dumpPy/266_'+track+'_BLT_service_id_with_datesJSON'
			this data should be put in /vasterasbuss.dev/bin/js/angular/hellspawn.js for the javascript being able to map the current date to which route_id for a specific buss. 

Step 3:
-------
	