# Thorp Builder Module

import random

def thorp():
    print("Building a Thorp. Please hold...")
    
    businesses = open(r"./textFiles/ThorpBusinesses.txt","r")
    fullBusinessList = []
    finalBusinessList = []
    
    for option in businesses:
    
        fullBusinessList.append(option)
        
    i = 1
    
    while i < 7:
    
        finalBusinessList.append(fullBusinessList[random.randint(0,7)])
        
        i += 1
        
    return finalBusinessList
    
    