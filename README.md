# CityPlanner

Welcome to the City Planner. This is a command line program that is helpful for worldbuilding in a fantasy medieval world.

This was built from a Google Sheet that I had put together as an idea for a random table and works as follows,

**The Lists:**

There are 8 different tables. Each table is named after a specific city size (Hamlet, Village, etc.) with each table containing a list of businesses that 
would be found in cities of those sizes. Each list contains either 6 or 8 options. This is done so that the math works out well when doing this 
in a physical environment with real dice. 

**The Logic:**

the rules for how to pick from a list change depending on what size city you would like to generate. This lets the list build off of itself in a neat way
so that the cities you generate build out their own histories and make sense when it comes to someone asking why a specific business is in an area. The 
rules mentioned are as follows,


 Town Sizes | Population Counts | Die Roll | 	Number of Businesses/Features                                                
|------------|---|---|-------------------------------------------------------------------------------|
 Thorp      |	20 - 80	      |   d6	  | Roll 5 times                                                                  
 Hamlet	    |    81 - 400	  |   d12	  | Roll 8 times                                                                  
 Village	   |    401 - 900	  |   d20	  | Roll 12 times                                                                 
 Small Town |	901 - 2000	  |   d20+6  | 	Roll 12 times. Include whatever you want from the Thorp table                
 Large Town |	2001 - 5000	  |   d20+12 | 	Roll 12 times. Include whatever you want from the Hamlet table and lower     
 Small City |	5001 - 12000  |   d20+20 | 	Roll 12 times. Include whatever you want from the Village table and lower    
 Large City |	12001 - 25000 |   d20+26 | 	Roll 12 times. Include whatever you want from the Small Town Table and lower 
 Metropolis |	25001+        |   d20+26 | 	Roll 16 times. Include whatever you want from the Small Town Table and lower 

This program serves as a codified version of the above that can be run from any system with python on it



=================================================================



Project Structure Starting Plan:

- A command line program that reads in from several text files (maybe one larger one with specific line seperations?)
	- done
- populate lists with data from the text files
	- done
- randomly select sommething from the list depending on user input
	- done
- output it all in some form (maybe new text file? command line print out is the easist)
	- command line for now
- main python file that handles all the executions
	- done
- smaller script/class files that deal with all the individual file reading
	- scrapped as was determined to not be the best way to go about it. All the functions make sense to be in the same area with each other and need to pass info back and forth

Parts needed for development:
- read in a file
- ask for user input
- parse read in information and populate lists with it
- output to file or cmd line