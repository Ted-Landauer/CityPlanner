import random
import re



class CityBuilder:

    #townList = []
    #fullList = []
    #finalList = []


    
    def __init__(self):
        self.townList = []
        self.fullList = []
        self.finalList = []
        self.extraTableNumber = 0



    def populateLists(self):

        townSizes = open(r"./textFiles/TownSizes.txt","r")
        thorp = open(r"./textFiles/ThorpBusinesses.txt","r")
        hamlet = open(r"./textFiles/HamletBusinesses.txt","r")
        village = open(r"./textFiles/VillageBusinesses.txt","r")
        smallTown = open(r"./textFiles/SmallTownBusinesses.txt","r")
        largeTown = open(r"./textFiles/LargeTownBusinesses.txt","r")
        smallCity = open(r"./textFiles/SmallCityBusinesses.txt","r")
        largeCity = open(r"./textFiles/LargeCityBusinesses.txt","r")


            
        for tb in thorp:
            if "\n" not in tb:
                tb = tb + "\n"
            
            self.fullList.append(tb)
            
        for hb in hamlet:
            if "\n" not in hb:
                hb = hb + "\n"
                
            self.fullList.append(hb)
            
        for vb in village:
            if "\n" not in vb:
                vb = vb + "\n"
                
            self.fullList.append(vb)
            
        for stb in smallTown:
            if "\n" not in stb:
                stb = stb + "\n"
                
            self.fullList.append(stb)
            
        for ltb in largeTown:
            if "\n" not in ltb:
                ltb = ltb + "\n"
                
            self.fullList.append(ltb)
            
        for scb in smallCity:
            if "\n" not in scb:
                scb = scb + "\n"
                
            self.fullList.append(scb)
            
        for lcb in largeCity:
            if "\n" not in lcb:
                lcb = lcb + "\n"
                
            self.fullList.append(lcb)
            


        for towns in townSizes:
            print(towns, end='')
            
            
            self.townList.append(towns)



    def buildCity(self, userInput):

        if userInput.upper() == "THORP":
            
            i = 1
            while i < 6:
                self.finalList.append(self.fullList[random.randint(0,5)])
                
                i += 1
                   
        elif userInput.upper() == "HAMLET":
            
            i = 1
            while i < 9:
                self.finalList.append(self.fullList[random.randint(0,11)])
                
                i += 1
                
        elif userInput.upper() == "VILLAGE":
            
            i = 1
            while i < 13:
                self.finalList.append(self.fullList[random.randint(0,19)])
                
                i += 1
                
        elif userInput.upper() == "SMALL TOWN":
            
            self.extraTableNumber = 1
            #more to do to this section
            i = 1
            while i < 13:
                self.finalList.append(self.fullList[random.randint(6,25)])
                
                i += 1
                               
        elif userInput.upper() == "LARGE TOWN":
            
            self.extraTableNumber = 2
            
            i = 1
            while i < 13:
                self.finalList.append(self.fullList[random.randint(12,31)])
                
                i += 1
                
        elif userInput.upper() == "SMALL CITY":
            
            self.extraTableNumber = 3
            
            i = 1
            while i < 13:
                self.finalList.append(self.fullList[random.randint(20,39)])
                
                i += 1
                
        elif userInput.upper() == "LARGE CITY":
            
            self.extraTableNumber = 4
            
            i = 1
            while i < 13:
                self.finalList.append(self.fullList[random.randint(26,45)])
                
                i += 1
                
        elif userInput.upper() == "METROPOLIS":
            
            self.extraTableNumber = 5
            
            i = 1
            while i < 17:
                self.finalList.append(self.fullList[random.randint(26,45)])
                
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
    
    def printResults(self, finalList):
    
        listBeginnings = 0
        print("Your town contains the following businesses...\n")

        for x in self.finalList:

            print(x)
            
        if self.extraTableNumber == 0:
            pass
            
        elif self.extraTableNumber == 1:
        
            print("-----Also, please select any number of the following options from the Thorp table-----\n")

            while listBeginnings < 6:
                print(self.fullList[listBeginnings], end='')
                listBeginnings += 1
        
        elif self.extraTableNumber == 2:
        
            print("-----Also, please select any number of the following options from the Hamlet and Thorp tables-----\n")
        
            while listBeginnings < 12:
                print(self.fullList[listBeginnings], end='')
                listBeginnings += 1
        
        elif self.extraTableNumber == 3:
        
            print("-----Also, please select any number of the following options from the Village, Hamlet, and Thorp tables-----\n")
        
            while listBeginnings < 20:
                print(self.fullList[listBeginnings], end='')
                listBeginnings += 1
        
        elif self.extraTableNumber > 3:
        
            print("-----Also, please select any number of the following options from the Small Town, Village, Hamlet, and Thorp tables-----\n")
            
            while listBeginnings < 26:
                print(self.fullList[listBeginnings], end='')
                listBeginnings += 1
        
            
    
    def retryGeneration(self, val):
        
        while True:
            
            redo = input("would you like to redo this town? [Y/N]: ")
            
            if redo.upper() == "Y":
                print("Understood. Try this one...\n")
                
                self.finalList.clear()
                
                self.buildCity(val)
                
                self.printResults(self.finalList)
                
            elif redo.upper() == "N":
                again = input("Got it. Do you want to do another town? [Y/N]: ")
                
                if again.upper() == "Y":
                
                    self.extraTableNumber = 0
                    
                    print("Coming right up\n")
                    
                    self.finalList.clear()
                    
                    self.main()
                    
                else:
                    print("Have a good day")
                    
                    break;
                
                break;
            else:
                print("Not sure what you mean there...")
                
        
    
    def main(self):
    
        print("Welcome to the City Planner!\n\nPlease select the size of the city you would like to create? Your options are...\n")
        
        self.populateLists()
        
        
        
        while True:
                
            val = input("\n\nSelection: ").title()
            
            r = re.compile(val)
            
            if list(filter(r.match, self.townList)):
                print("You've selected a " + val + ". Please hold while I build your city\n")
                break;
            else:
                print("I'm sorry. That doesn't seem to be an option. Please try again")
                 
        
        self.buildCity(val)
        self.printResults(self.finalList)
        self.retryGeneration(val)
        
        
    
    
    
Object = CityBuilder()
Object.main()