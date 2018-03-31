# Nick Caspers
# Dec 29, 2017
#####################################################################################

# Config class
# Handles the reading of configuration files and the holding of their parameteres

class Config:

    # Data Members
    configPath = ""
    sandboxMode = True
    rootTweetID = ""
    scriptPath = ""
    jsonPath = ""
    logPath = ""
    
    ###########################################################
    # Constructor (should just leave it as a default constructor)

    # Read config file and set datamembers
    @staticmethod
    def readConfig(configPath):
        
        # set the config path
        Config.configPath = configPath
        configFile = open(configPath, 'r')

        # read in the file
        currentLine = ""
        currentLine = configFile.readline()

        while(currentLine):

            currentLine = currentLine.translate(None, "\n")

            # determine if a line is not a comment
            if(len(currentLine) == 0 or currentLine[0] == "#"):
                currentLine = configFile.readline()
                continue

            if(currentLine == "-Sandbox Mode-"):
                
                # Sand box tag
                currentLine = configFile.readline()
                currentLine = currentLine.translate(None, "\n")
                Config.sandboxMode = (currentLine == "ON") or (currentLine == "1")
    
            elif(currentLine == "-Root Tweet-"):

                # Rott Tweet ID
                currentLine = configFile.readline()
                currentLine = currentLine.translate(None, "\n")
                Config.rootTweetID = currentLine

            elif(currentLine == "-Script Path-"):

                # Script path tag
                currentLine = configFile.readline()
                currentLine = currentLine.translate(None, "\n")
                Config.scriptPath = currentLine

            elif(currentLine == "-JSON Path-"):
    
                # JSON path tag
                currentLine = configFile.readline()
                currentLine = currentLine.translate(None, "\n")
                Config.jsonPath = currentLine

            elif(currentLine == "-Log Path-"):

                # Log path tag
                currentLine = configFile.readline()
                currentLine = currentLine.translate(None, "\n")
                Config.logPath = currentLine

            # increment to the next line
            currentLine = configFile.readline()


        # check the configuration reading
        print("ConfigPath: " + Config.configPath)
        print("Sandbox Mode? " + str(Config.sandboxMode))
        print("Root Tweet ID: " + Config.rootTweetID)
        print("Script Path: " + Config.scriptPath)
        print("JSON Path: " + Config.jsonPath)
        print("Log Path: " + Config.logPath)


    ############################################################
    # Object Methods
        
    ############################################################
    # Getters and Setters
    
    ############################################################
    # toString Methods 
