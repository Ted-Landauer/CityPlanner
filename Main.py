import ThorpBuilder

print("Welcome to the City Planner!\n\nPlease select the size of the city you would like to create? Your options are...\n")

townSizes = open(r"./textFiles/TownSizes.txt","r")
townList = []


for towns in townSizes:
    print(towns, end='')
    
    townList.append(towns)
    

val = input("\n\nSelection: ")

print("You've selected a " + val)

if val.upper() == "THORP":

    
    print(ThorpBuilder.thorp())
    
    


