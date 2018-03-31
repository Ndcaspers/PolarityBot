# Nick Caspers
# Dec 1, 2017
#####################################################################################

# Tweet class
# Maintains the surface level data of a tweet.
# Note: Surface level data includes data from a standard /statuses/show.json?id=___

import json

import tweepy
from UsingTweepy import UsingTweepy

#from textblob import TextBlob

class Tweet:

    # Data Members
    tweetID = 0
    creationDate = ""
    userName = ""
    userID = 0
    text = ""
    unicodeText = ""
    retweetCount = 0
    favoriteCount = 0

    isReply = False
    replyToStatusID = None

    shortURL = ""

    textBlobSentiment = None
    polarity = 0
    subjectivity = 0

    ###########################################################
    # Constructor (should just leave it as a default constructor)

    # Setting the Data Members
    def setAspects(self, tweetID, creationDate, 
                        userName, userID,
                        text, retweetCount, favoriteCount, 
                        isReply, replyToStatusID):
        
        # Generic Initialization
        self.tweetID = tweetID
        self.creationDate = creationDate
        self.userName = userName
        self.userID = userID
        self.text = text.encode('ascii','ignore')
        self.unicodeText = text
        self.retweetCount = retweetCount
        self.favoriteCount = favoriteCount
        self.isReply = isReply
        self.replyToStatusID = replyToStatusID

    ############################################################
    # Object Methods
        
    ############################################################
    # Getters and Setters
    def setPolarityValues(self, polarity, subjectivity):

        # Parse out the values from the textBlob sentiment stuff
        #self.textBlobValues = polarityValues
        self.polarity = polarity
        self.subjectivity = subjectivity


    def getLink(self):

        # construct the html link
        htmlLink = "https://twitter.com/" + self.userName + "/status/" + str(self.tweetID)
        return htmlLink

    ############################################################
    # toString Methods
    def toString(self):
    
        # Because muli-line string concatentation doesnt exist in python
        report = "TweetID: " + str(self.tweetID) + "\n"
        report = report + "UserName: " + str(self.userName) + " (id: " + str(self.userID) + ")\n"
        report = report + "\tText: \"" + str(self.text) + "\"\n"
        report = report + "\tRetweets: " + str(self.retweetCount) + ", Favorites: " + str(self.favoriteCount) + "\n"
        report = report + "\tcreated: " + str(self.creationDate) + "\n"
        report = report + "\tisReply? " + str(self.isReply) + ", To? " + str(self.replyToStatusID) + "\n"
                       
        return report


