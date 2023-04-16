#!/bin/bash
#python /home/vnkehrer/Documents/SeniorProject/blue_hydra/search.py
#logfile=/home/vnkehrer/Documents/SeniorProject/blue_hydra/blue_hydra_rssi_search.log


read -p "Enter MAC address: " MAC #asks user for an input aka the target mac address

echo "MAC: $MAC" 

#loop search.py until target is found
while true; do

	echo "loop"
	
    python3 search.py $MAC #passes to python file

    STATUS=`cat .found.txt`
    if [ "$STATUS" == "true" ]; then
        break
    fi


    date +"%D %r" #gives local time
	sleep 2 #sleep 2 seconds before searching again
done
