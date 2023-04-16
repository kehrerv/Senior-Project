#!/bin/bash

#./bin/blue_hydra > /dev/null 2>&1 #catches output and any error messages into the void aka

gnome-terminal --command="./bin/blue_hydra"
sleep 10

./rerun.sh
