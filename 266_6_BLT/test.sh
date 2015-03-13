awk 'BEGIN {FS=","} 
				{ 
					print $0
				} 
				' ../calendar.txt
	