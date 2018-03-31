# Nick Caspers
# Dec 7, 2017
#################################

# JSONReader class
# Purpose is to provide different methods of reading an json file
# For instance, if its the json of a regular tweet, a set of retweets, or usernames


import json
from Tweet import Tweet


class JSONReader:

    ###########################
    # Static Methods for Gathering Tweet Information
    @staticmethod
    def standardTweet(tweetObject, outputJSON):

        # Obtain the data in the json
        jsonData = json.load(open(outputJSON, 'r'))

        # Parse the json info and fill tweet
        JSONReader.parseStandardInfo(tweetObject, jsonData)
       

    @staticmethod
    def setOfReplies(rootTweetID, outputJSON, tweetList):

        # Load in the JSON data
        jsonData = json.load(open(outputJSON, 'r'))
        statuses = jsonData["statuses"]
        maxID = jsonData["search_metadata"]["max_id"]

        # Need smallest id
        smallID = maxID

        # Should run through the potential set of replies, and pull out the cvalid ones
        for status in statuses:

            # Check if it replies to the wanted tweet
            replyID = status["in_reply_to_status_id"]
            
            if (replyID == rootTweetID):
       
                # Aight the tweet is a reply to the root tweet
                tempTweet = Tweet()
                tweetList += [tempTweet]

                # now grab and parse all the given information (most likely standard)
                JSONReader.parseStandardInfo(tweetList[-1], status)

            if (status["id"] < smallID):
                smallID = status["id"]

        # max id can be easily grabbed, so return it
        return [smallID, len(statuses)]


    #############################################
    # Helper Static methods
    @staticmethod
    def parseStandardInfo(tempTweet, jsonData):

        # Parse info
        tweetID = jsonData["id"]
        created = jsonData["created_at"]

        userName = jsonData["user"]["screen_name"]

        userID = jsonData["user"]["id"]

        text = jsonData["text"]

        retweetCount = jsonData["retweet_count"]

        favoriteCount = jsonData["favorite_count"]

        replyToStatusID = jsonData["in_reply_to_status_id"]

        isReply = not(replyToStatusID == None)

        # fill in the temp tweet
        tempTweet.setAspects(tweetID, created,
                                    userName, userID,
                                    text, retweetCount, favoriteCount,
                                    isReply, replyToStatusID)
       


