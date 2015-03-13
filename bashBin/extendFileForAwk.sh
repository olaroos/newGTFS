
while read line 
do echo $line"," | tr -d "\n" | tr -d "\r" >> tmpCalendar.txt;
echo "" >> tmpCalendar.txt
done < "../calendar.txt"
mv tmpCalendar.txt ../calendar.txt

# rm tmpCalendar.txt
# while read line 
# do echo $line"," | tr -d "\n" | tr -d "\r" >> tmpCalendar.txt;
# echo "" >> tmpCalendar.txt
# done < "../calendar_dates.txt"
# mv tmpCalendar.txt ../calendar_dates.txt
# rm tmpCalendar.txt