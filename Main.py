#!/bin/python
###############################################################
# Nick Caspers
# December 1, 2017
##############################################################

# Main File
# Used for testing and running the essential features of the Polarity Bot Project

import os;
import sys
import json;


from Config import Config
from KeyBank import KeyBank
from FindTweets import FindTweets
from JSONReader import JSONReader
from UsingTweepy import UsingTweepy
from Tweet import Tweet
from TweetAnalyzer import TweetAnalyzer
from Log import Log

def main():

    # Determine if configuration path is there
    if(len(sys.argv) != 2):
        
        # needs to be a path in the first argument
        print("Error: No Configuration Path given...")
        return 1

    # Read in the configuration file 
    print(sys.argv[1])
    Config.readConfig(sys.argv[1])

    # Make sure tweepy and the key bank is set up
    KeyBank.setup()
    UsingTweepy.setup()

    # Pull in the root tweet
    print("Standard Tweet Pull Test")

    tweetID = Config.rootTweetID
    outputJSON = Config.jsonPath + "PY_Tweet.json"

    print(" ")
    print("Obtain Tweet: " + tweetID)
    print("OutputFile: " + outputJSON)

    emptyTweet = Tweet()
    FindTweets.oneTweet(emptyTweet, tweetID, outputJSON)

    # Check Tweet
    print("Checking Pulled Tweet...")
    print(emptyTweet.toString())

    # Second Test, reply test
    print(" ")
    print("Reply Tweets Pull Test")
    print("======================")

    rootTweet = emptyTweet
    replyJSON = Config.jsonPath + 'ReplyTweets.json'

    replyList = []
    FindTweets.replyTweets(rootTweet, replyJSON, replyList)

    print("Complete.")
    print("Amount of Replies: " + str(len(replyList)))

    # Third Test, polarity parsing
    print(" ")
    print("Polarity Test")
    print("========================")

    tweetAnalyzer = TweetAnalyzer(rootTweet, replyList)
    tweetAnalyzer.compilePolarity()

    print(" ")
    print(" ")
    print("========================")
    print("Polarity of Root Tweet:")
    print("\tPolarity: " + str(tweetAnalyzer.avgPolarity) + " (std: " + str(tweetAnalyzer.stdPolarity) + ")")
    print("\tSubjectivity: " + str(tweetAnalyzer.avgSubjectivity) + " (std: " + str(tweetAnalyzer.stdSubjectivity) + ")")
    print("\tPercent Polarities: " + str(round(tweetAnalyzer.percentPos, 2)) + " - " + str(round(tweetAnalyzer.percentNeut, 2))) + ' - ' + str(round(tweetAnalyzer.percentNeg, 2))

    print("Complete.")

    # Word Frequency Test
    print(" ")
    print("Word Frequency Test")
    print("========================")

    tweetAnalyzer.compileWordFreq()

    # probably need a function to toString it or output the top three words, ignoring obvious shit
    print(" ")
    print(tweetAnalyzer.toStringHighWordFreq())
    
    print("Complete.")

    # Commence to show the logging test
    print(" ")
    print("Log Test")
    print("========================")
    print(" ")

    print("Replies: ")
    print(tweetAnalyzer.toStringSentimentReply())
    print(tweetAnalyzer.toStringFreqReply())
    print(" ")
    print("tweet length 1: " + str(len(tweetAnalyzer.toStringSentimentReply())))
    print("tweet length 2: " + str(len(tweetAnalyzer.toStringFreqReply())))
    print(" ")
    print("Notice: \n" +  tweetAnalyzer.toStringUpdate())
    print(" ")

    print("Complete.")

    if(Config.sandboxMode):

        # in sandbox, therefore do not send tweets
        print(" ")
        print("(In Sandbox Mode)")
        print("Testing Complete")
        print("========================")

    else:

        # in production mode, send tweets and update the log
        print(" ")
        print("(In Production Mode)")
        print("Sending Tweets")
        print("========================")

        # send the tweet regarding sentiment analysis
        UsingTweepy.sendReply(tweetAnalyzer.toStringSentimentReply(), tweetAnalyzer.rootTweet.tweetID)

        # send the tweet regarding word frequency
        UsingTweepy.sendReply(tweetAnalyzer.toStringFreqReply(), tweetAnalyzer.rootTweet.tweetID)

        # send notice of new analysis
        UsingTweepy.sendTweet(tweetAnalyzer.toStringUpdate())

        print("Complete. (Check Twitter)")
    
        print(" ")
        print("Logging Analysis")
        print("=======================")
        print(" ")

        # setup the log paths
        logFilePath = Config.logPath
        Log.setup(logFilePath)

        # write in the tweet analysis
        Log.logAnalysis(tweetAnalyzer)

        print("Complete. (Check Log)")
        print("Production Complete.")
        print("========================")







##################################################################
# Just Running the program

if __name__ == "__main__":
	
    print("Running Main...\n")
    main()
