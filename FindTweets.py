# Nick Caspers
# Dec 1, 2017
######################################

# Find Tweets class
# A place holder for functions meant to find a specific subset of tweets

import os
import time

from Config import Config
from KeyBank import KeyBank
from JSONReader import JSONReader
from Tweet import Tweet
from Stopwatch import Stopwatch

class FindTweets:

    # Data memebers (probably none)

    ######################################
    # Constructor (probably just default)

    ######################################
    # Methods ( most likely just static stuff )

    ######################################################
    @staticmethod
    def oneTweet(emptyTweet, tweetID, outputJSON):
        
        # Pull that one tweet's json file
        genericPath = Config.scriptPath + 'PullTweet.sh'
        os.system(genericPath + ' ' + tweetID + ' ' + KeyBank.getKey() + ' ' + outputJSON)

        # Read in tweet, from file, and into empty tweet
        JSONReader.standardTweet(emptyTweet, outputJSON)
        
     
    ######################################################
    @staticmethod
    def replyTweets(rootTweet, outputJSON, replyList):

        # With the rootTweet, should be able to get replies
        # Parse rootTweet for the accountName and the tweetID
        rootAccountName = rootTweet.userName
        rootTweetID = rootTweet.tweetID
        rootDate = rootTweet.creationDate

        # pull the data and parse into the various tweets
        currentTweetList = []

        amountOfTweets = 100
        maxID = -1 
        genericPath = Config.scriptPath + 'PullReplies.sh'

        # Make sure to start the timer
        stopwatch = Stopwatch()
        stopwatch.startTime()

        iteration = 0
        while(amountOfTweets == 100):

            # Now Pull for tweeets
            os.system(genericPath + ' ' + rootAccountName + ' ' + str(maxID) + ' ' + str(rootTweetID) + ' ' + KeyBank.getKey() + ' ' + outputJSON)

            # Read in the tweets, aka run through the replies proposed
            jsonOutputList = []
            jsonOutputList = JSONReader.setOfReplies(rootTweetID, outputJSON, currentTweetList)
            replyList += currentTweetList

            # Determine the amount of tweets
            maxID = jsonOutputList[0] - 1 
            amountOfTweets = jsonOutputList[1] 
            
            # check the elapsed time and the iterations
            print("Iteration: " + str(iteration) + ", (Elapsed Time: " + str(stopwatch.elapsedTime()) + ")")
            if((iteration >= 448 and KeyBank.bankIndex == 0) or iteration >= 449):
            
                # stop the program until 15 minutes has passed or switch the keys used to access
                KeyBank.changeKeys()

                # might have wrapped around the keybank
                if(stopwatch.elapsedTime() < (15.0 * 60.0) and KeyBank.bankIndex == 0):

                    # If so just sleep the last part of the 15 min
                    fifteen_min = (15 * 60.0) + 30
                    time.sleep(fifteen_min - stopwatch.elapsedTime())

                    # reset the clock
                    stopwatch.startTime()
                
                # reset the iterations for the next key
                iteration = 0 

            # increments and resets
            currentTweetList = []
            iteration += 1


    @staticmethod
    def modifyDate(date):
        
        # Tokenizee date, and reconfigure
        dateTokens = date.split(" ")
        newDate = dateTokens[0] + " " + dateTokens[1] + " " + dateTokens[2] + " " + dateTokens[5]
        
        # reformat the date given
        dateObj = time.strptime(newDate, "%a %b %d %Y")
        modifiedDate = time.strftime("%Y-%m-%d", dateObj)

        return modifiedDate


