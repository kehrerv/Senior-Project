#!/bin/bash
#python /home/vnkehrer/Documents/SeniorProject/blue_hydra/search.py
#logfile=/home/vnkehrer/Documents/SeniorProject/blue_hydra/blue_hydra_rssi_search.log



#stopwatch
start=$(date +%s)
while true; do
    time="$(($(date +%s) - $start))"
    printf '%s\r' "$(date -u -d "@$time" +%H:%M:%S)"
done
#---------------------------------

echo "Starting search..."

#loop search.py until target is found
while true; do

	echo "loop"
	if python search.py | grep EE:82:30:92:BC:64  >> blue_hydra_rssi_search.log 2>&1; then
		echo "output found!"
		date +"%D %r" #gives local time
		break
	else
		echo "Searching..."
	fi

	#echo "Searching..."
	sleep 2 #sleep 2 seconds before searching again
done

:'

while :
do

	date +"%D %r" #>> blue_hydra_rssi_search.log #gives local time
	echo "loop"
	#send the output of the pyhon program to the logfile and put the error output in the logfile too
	python search.py >> blue_hydra_rssi_search.log 2>&1
	#77:54:7F:C1:1B:32
	
	sleep 2

done
'




