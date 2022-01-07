import ThorpBuilder
import HamletBuilder
import random

print("Welcome to the City Planner!\n\nPlease select the size of the city you would like to create? Your options are...\n")

townSizes = open(r"./textFiles/TownSizes.txt","r")
thorp = open(r"./textFiles/ThorpBusinesses.txt","r")
hamlet = open(r"./textFiles/HamletBusinesses.txt","r")
village = open(r"./textFiles/VillageBusinesses.txt","r")
smallTown = open(r"./textFiles/SmallTownBusinesses.txt","r")
largeTown = open(r"./textFiles/LargeTownBusinesses.txt","r")
smallCity = open(r"./textFiles/SmallCityBusinesses.txt","r")
largeCity = open(r"./textFiles/LargeCityBusinesses.txt","r")

townList = []
fullList = []
finalList = []


    
    
for tb in thorp:
    if "\n" not in tb:
        tb = tb + "\n"
    
    fullList.append(tb)
    
for hb in hamlet:
    if "\n" not in hb:
        hb = hb + "\n"
        
    fullList.append(hb)
    
for vb in village:
    if "\n" not in vb:
        vb = vb + "\n"
        
    fullList.append(vb)
    
for stb in smallTown:
    if "\n" not in stb:
        stb = stb + "\n"
        
    fullList.append(stb)
    
for ltb in largeTown:
    if "\n" not in ltb:
        ltb = ltb + "\n"
        
    fullList.append(ltb)
    
for scb in smallCity:
    if "\n" not in scb:
        scb = scb + "\n"
        
    fullList.append(scb)
    
for lcb in largeCity:
    if "\n" not in lcb:
        lcb = lcb + "\n"
        
    fullList.append(lcb)
    


for towns in townSizes:
    print(towns, end='')
    
    
    townList.append(towns)
    

val = input("\n\nSelection: ")

print("You've selected a " + val + ". Please hold while I build your city\n")



if val.upper() == "THORP":
    
    i = 1
    while i < 6:
        finalList.append(fullList[random.randint(0,5)])
        
        i += 1
           
elif val.upper() == "HAMLET":
    
    i = 1
    while i < 9:
        finalList.append(fullList[random.randint(0,11)])
        
        i += 1
        
elif val.upper() == "VILLAGE":
    
    i = 1
    while i < 13:
        finalList.append(fullList[random.randint(0,19)])
        
        i += 1
        
elif val.upper() == "SMALL TOWN":
    
    #more to do to this section
    i = 1
    while i < 13:
        finalList.append(fullList[random.randint(6,25)])
        
        i += 1
        
elif val.upper() == "LARGE TOWN":
    
    i = 1
    while i < 13:
        finalList.append(fullList[random.randint(12,31)])
        
        i += 1
        
elif val.upper() == "SMALL CITY":
    
    i = 1
    while i < 13:
        finalList.append(fullList[random.randint(20,39)])
        
        i += 1
        
elif val.upper() == "LARGE CITY":
    
    i = 1
    while i < 13:
        finalList.append(fullList[random.randint(26,45)])
        
        i += 1
        
elif val.upper() == "METROPOLIS":
    
    i = 1
    while i < 17:
        finalList.append(fullList[random.randint(26,45)])
        
        i += 1
    
else:
    print("That settlement size doesn't exist. Please try again")

'''
print("\n\n-----space for test print-----\n\n")

i = 1

print(fullList)
for x in fullList:
    
    print(str(i) + ": " + x)
    i += 1
'''


  
print("Your town contains the following businesses...\n")

for x in finalList:
    
    print(x)

