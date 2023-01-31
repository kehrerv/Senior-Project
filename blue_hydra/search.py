#!usr/bin/env python
import os



#opens file to read "r"
with open(r"blue_hydra_rssi.log", "r") as file:
    x = input("Enter target Mac address: ")

    #reads all the content from the file
    content = file.readlines()[10] #reads from a particular line from []
    characterNum = len(content)
    print("Selected line content: ", content)
    print("number of characters: ", characterNum)
        
    one, two, mac, rssi = content.split()
    print("BT MAC: ", mac)
    print("RSSI: ", rssi)



    #searches if the input is present in the text
    if x in content:
        print("string exist")

       # print(content)
        print(x)
    else:
        print("string does not exist")
    
    

    


