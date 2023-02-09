#!usr/bin/env python
import os




#opens file to read "r"
with open(r"blue_hydra_rssi.log", "r") as file:


    x = input("Enter target Mac address: ")

    def lineCount(x):
        for x in enumerate(file):
            if x in line:
                print ("Line #: ", i)
                return i
        return -1




    #reads all the content from the file
    #content = file.readlines()[10] #reads from a particular line from []
    
    content = file.read() #reads from a particular line from []
    characterNum = len(content)
        

    #print("number of characters: ", characterNum)
    
    


    #line counter
    line_num = 0
    for line in file.readlines():
        line_num += 1
        if line.find(x) >= 0:
            print ("line number: ",line_num)
#--------------------------------------

    #turning the file into a list
    data_into_list = content.split("\n")
    #searched = content.find(x)
    #second = searched+1
    #print("Target index at: ",searched)
    #print("Second index at: ",second)
    #print(data_into_list.index[x])
    for i in data_into_list:
        if x in i:
            word=str(i)
            word = word.split(" ")
            rssi = word[3] 
            
            print("MAC Address: ",word[2])
            print("RSSI: ",rssi)


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
    
    

    


