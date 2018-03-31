# Nick Caspers
# Dec 7, 2017
#####################################################################################

# Log class
# Logs tweets into a particular file, dictated by the configuration file

import time

from Tweet import Tweet

class Log:

    # Data Members 
    logFile = ""

    ###########################################################

    # Constructor ( probably leave as default )

    # Setup the log file
    @staticmethod
    def setup(filePath):
    
        # set the log file path
        Log.logFile = filePath


    ############################################################
    #Class Methods

    @staticmethod
    def logTweet(tweet):

        # log given tweet into the ouptut file
        openLog = open(Log.logFile, "a")

        # write the data of the given file in 
        openLog.write(tweet.toString())
        openLog.write("\n")

        openLog.close()


    @staticmethod
    def logAnalysis(tweetAnalyzer):

        # log the tweet analyzer
        openLog = open(Log.logFile, "a")

        openLog.write("Entry: " + str(tweetAnalyzer.latestEntryNum() + 1) + "\n")
        openLog.write("---------------------------")
        openLog.write(time.strftime("%Y-%m-%d %H:%M:%S") + "\n")

        openLog.close()

        # first write in the root tweet
        Log.logTweet(tweetAnalyzer.rootTweet)

        # then write int he analyzer data
        openLog = open(Log.logFile, "a")

        openLog.write(tweetAnalyzer.toString())

        openLog.close()

        # also write the response dictated by the analyzer data
        Log.logResponse(tweetAnalyzer.toStringSentimentReply() + "\n" + tweetAnalyzer.toStringFreqReply())

        openLog = open(Log.logFile, "a")

        openLog.write("\n")

        openLog.close()


    @staticmethod
    def logResponse(response):

        # note the response whould just be some string of the tweet status update
        openLog = open(Log.logFile, "a")
        
        openLog.write("\n\nResponse:\n" +  response + "\n")

        openLog.close()
      


    ############################################################
    # Getters and Setters

    ############################################################
    # toString Methods


