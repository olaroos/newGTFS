# cat ../calendar.txt | awk 'BEGIN {FS=","} 
# {
# 	print $0 
# }' | echo "," >> tmpCalendar.txt
rm tmpCalendar.txt
while read line 
do echo $line"," | tr -d "\n" | tr -d "\r" >> tmpCalendar.txt;
echo "" >> tmpCalendar.txt
done < "../calendar.txt"