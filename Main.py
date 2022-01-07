import random
import re



class CityBuilder:

    #initializations
    def __init__(self):
        self.townList = []
        self.fullList = []
        self.finalList = []
        self.extraTableNumber = 0


    #function to read in the text files needed for the program
    def populateLists(self):

        #all the text files!
        townSizes = open(r"./textFiles/TownSizes.txt","r")
        thorp = open(r"./textFiles/ThorpBusinesses.txt","r")
        hamlet = open(r"./textFiles/HamletBusinesses.txt","r")
        village = open(r"./textFiles/VillageBusinesses.txt","r")
        smallTown = open(r"./textFiles/SmallTownBusinesses.txt","r")
        largeTown = open(r"./textFiles/LargeTownBusinesses.txt","r")
        smallCity = open(r"./textFiles/SmallCityBusinesses.txt","r")
        largeCity = open(r"./textFiles/LargeCityBusinesses.txt","r")


        #fill in the main full list of businesses in towns one at a time
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

        #fill in the list of different town sizes and print it
        for towns in townSizes:
            print(towns, end='')
            
            self.townList.append(towns)


    #function to build out the actual city business lists
    def buildCity(self, userInput):

        #check if the sanitized user input matches the options available
        if userInput.upper() == "THORP":
            
            #randomly add a business from the matching list, duplicates are expected and wanted
            i = 1
            while i < 6:
                self.finalList.append(self.fullList[random.randint(0,5)])
                
                i += 1
                
        #following code blocks are similar in function and design to the one above. Future comments omitted
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
            
            #set the value used to identify which table we need to provide all the options for
            self.extraTableNumber = 1
            
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
            #if the user some how gets past our sanitizing of inputs this should catch anything else. Also denotes when something is wrong in the matching code
            print("That settlement size doesn't exist. Please try again")

    
    #function to print out the final set of results
    def printResults(self, finalList):
    
        #reset this value for repeat runs
        listBeginnings = 0
        print("Your town contains the following businesses...\n")

        #print out the list of appropriate businesses
        for x in self.finalList:
            print(x)
            
        #check if we do not need to include extra options
        if self.extraTableNumber == 0:
            pass
            
        elif self.extraTableNumber == 1:
        
            print("-----Also, please select any number of the following options from the Thorp table-----\n")

            #list out the extra options
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
        
            
    #function for handling the retry portion of the program in case the user wants to keep generating the same city or a different size
    def retryGeneration(self, val):
        
        while True:
            
            redo = input("would you like to redo this town? [Y/N]: ")
            
            #check if user wants to regenerate the same city
            if redo.upper() == "Y":
                print("Understood. Try this one...\n")
                
                #call the needed functions
                self.finalList.clear()
                
                self.buildCity(val)
                
                self.printResults(self.finalList)
                
            elif redo.upper() == "N":
                again = input("Got it. Do you want to do another town? [Y/N]: ")
                
                #check if the user wants to generate a different city type
                if again.upper() == "Y":
                    
                    #set values and call needed functions
                    self.extraTableNumber = 0
                    
                    print("Coming right up\n")
                    
                    self.finalList.clear()
                    
                    self.main()
                    
                #exit out if the user wants to end it
                else:
                    print("Have a good day")
                    
                    break;
                
                break;
                
            #catch the user putting in incorrect data and reprompt
            else:
                print("Not sure what you mean there...")
                
        
    #main function that handles all executions
    def main(self):
    
        #greet user and build out the lists
        print("Welcome to the City Planner!\n\nPlease select the size of the city you would like to create? Your options are...\n")
        
        #clear the list for repeat run when generating a new city type
        self.fullList.clear()
        self.populateLists()     
        
        #keep running for input
        while True:
                
            #grab user input
            val = input("\n\nSelection: ").title()
            
            #set up regex for use in verifying that the user input a value that exists
            r = re.compile(val)
            
            #kick it off
            if list(filter(r.match, self.townList)):
                print("You've selected a " + val + ". Please hold while I build your city\n")
                break;
            
            #prompt for retry on user error
            else:
                print("I'm sorry. That doesn't seem to be an option. Please try again")
                 
        #call necessary functions
        self.buildCity(val)
        self.printResults(self.finalList)
        self.retryGeneration(val)
        

Object = CityBuilder()
Object.main()