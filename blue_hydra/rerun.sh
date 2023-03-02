#!/bin/bash
python /home/vnkehrer/Documents/SeniorProject/blue_hydra/search.py


while :
do

	date +"%D %r" >> blue_hydra_rssi_search.log #gives local time
	echo "loop"
	#send the output of the pyhon program to the logfile and put the error output in the logfile too
	python search.py | echo "0A:A3:B1:F5:32:A1"  >> blue_hydra_rssi_search.log 2>&1
	
	sleep 2
done
