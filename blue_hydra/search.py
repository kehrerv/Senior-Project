#!usr/bin/env python
import os




#opens file to read "r"
with open(r"blue_hydra_rssi.log", "r") as file:

    #user enters the target's mac address here
    x = input("Enter target Mac address: ")



    #reads all the content from the file
    #content = file.readlines()[10] #reads from a particular line from []
    
    content = file.read() #reads from a particular line from []
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
            
            print("MAC Address: ",word[2]) #mac address is stored at index 2
            print("RSSI: ",rssi)
            
            #task: 
            #find a way to have mac address print only one time with maybe an if statement since it currently prints as many times as it finds a new rssi

#-------------------------------------

    #searches if the input is present in the text
    if x in content:
        print("SEARCH FOUND!") 
        

        '''
        one, two, mac, rssi = x.split()
        print("one: ", one)
        print("two: ", two
        print("BT MAC: ", mac)
        print("RSSI: ", rssi)
        
        print("Selected line content: ", content)
        print("input: ",x)'''
    else:
        print("SEARCH NOT FOUND!")
    
    

    


