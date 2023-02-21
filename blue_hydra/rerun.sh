#!/bin/bash
python /home/vnkehrer/Documents/SeniorProject/blue_hydra/search.py

while :
do

	date +"%D %r"
	#date +"%r"
	echo "loop"
	python search.py >> blue_hydra_rssi.log >%1

	sleep 2
done
