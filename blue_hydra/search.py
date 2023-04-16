#!usr/bin/env python3
import os
import sys

x = sys.argv[1] #recieves the input mac address from the rerun script
print("testing: ", x)
#opens file to read "r"
with open(r"blue_hydra_rssi.log", "r") as file:
    with open (".found.txt", "w") as f:

        check = False



        #reads all the content from the file
        
        content = file.read() #reads from a particular line if using []
        characterNum = len(content)
            

        #line counter
        line_num = 0
        for line in file.readlines():
            line_num += 1
            if line.find(x) >= 0:
                print ("line number: ",line_num)

    #--------------------------------------

        #turning the file into a list
        data_into_list = content.split("\n")
        #iterates through each index
        for i in data_into_list:
            #searches if the target is in one of these indexes
            if x in i: 
                word=str(i) #converts the specified index into a string
                word = word.split(" ") #separates the line into the 4 indexes
                rssi = word[3] #rssi is stored at index 3
                
                print("RSSI: ",rssi)
                
        #prints the MAC address only once if found 
        for b in data_into_list:
            if x in b:
                print("MAC Address: ",word[2]) #mac address is stored at index 2
                break

    #-------------------------------------

        #searches if the input is present in the text
        if x in content:
            print("SEARCH FOUND!")
            f.write("true")
        else:
            print("SEARCH NOT FOUND!")
            f.write("false")
        
