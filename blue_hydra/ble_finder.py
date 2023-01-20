#!/usr/bin/env python
#!~/Documents/SeniorProject/blue_hydra

#----------------------------------------------
# ble_finder.py
#    Authors: Troy Brown (@waveguyd) and Garrett Gee (@ggee)
#    Developed for:
#      http://hackerwarehouse.com / @hackerwarehouse
#      http://hackerwarehouse.tv
#
# requirements:
#   run from blue_hydra directory and rssi file output option enabled
#   tailer module
#
# todo:
#   foxhunting
#   change last seen to dd:hh:mm:ss
#----------------------------------------------

import datetime, os
from time import sleep

import tailer
 
devices = [
['78:46:D4:63:CE:DE', 'Valerie phone test', ''],
['2C:41:A1:8E:2E:59', 'mini child bose speaker', ''],
]

# threshold for reporting in seconds
#seenthreshold = 10
seenthreshold = 45

for line in tailer.follow(open("blue_hydra_rssi.log")):
	for idx, (mac, name, lastseen) in enumerate(devices):
		if mac in line:
			currentseen = float(line.split()[0])
			if lastseen:
				lastseen = float(lastseen)			
				tdelta = datetime.datetime.fromtimestamp(currentseen) - datetime.datetime.fromtimestamp(lastseen)
				tsec = tdelta.total_seconds()
				if tsec >= seenthreshold:
					print (mac) # + ' (' + mac + ') is nearby - last seen ' + str(tsec) + ' seconds ago'
                    print "hello" 
					# print name + ' (' + mac + ') is nearby - last seen ' + str(tsec) + ' seconds ago'
#					os.system('aplay ping.wav &')
			else:
				# first time seen
				print (name) # + ' (' + mac + ') is nearby'
#				os.system('aplay ping.wav &')

			# update last seen field with current timestamp
			devices[idx][2] = currentseen
