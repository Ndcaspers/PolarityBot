# Nick Caspers
# Dec 7, 2017
#####################################################################################

# UsingTweepy class
# Basically provides a wrapper around tweepys library

import tweepy

class UsingTweepy:

    # Data Members (basically just need the authorization aspects, broken up into sets)
    consumerKey = "95h2HaYKF5bP6eImSoWoP6NGV"
    consumerSecret = "VuIWaPjPibkha0jxDSVdGEFvUy6DKHBjnBzIb56Pb3rn8vY11p"
    accessToken = "944986499749236736-eO7fSLMT4wNjSCuT77MD72yuvxVO6zk"
    accessTokenSecret = "3IXb15wKJJVpySczOqRIIjau5tuH48MH1DiuLOLp8VATM"

    api = None

    ###########################################################

    # Constructor ( probably leave as default )

    # Setup Tweepy
    @staticmethod
    def setup():
    
        # set up the auth and api aspects
        # OAuth process, using the keys and tokens
        auth = tweepy.OAuthHandler(UsingTweepy.consumerKey, UsingTweepy.consumerSecret)
        auth.set_access_token(UsingTweepy.accessToken, UsingTweepy.accessTokenSecret)
 
        # Creation of the actual interface, using authentication
        UsingTweepy.api = tweepy.API(auth)

    ############################################################
    # Static API Methods

    @staticmethod
    def sendTweet(status):

        # Send message
        UsingTweepy.api.update_status(status)

    @staticmethod
    def sendReply(status, replyID):

        # sendREply assume status has the op in it already
        UsingTweepy.api.update_status(status, replyID)

    @staticmethod
    def sendSelfDM(message, userID):

        # probably just use tweepy to send self dm of url message
        api.send_direct_message(userID, message)

