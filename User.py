# Nick Caspers
# Dec 14, 2017
#####################################################################################

# User Class
# Acts as a holder for a user or an account

from Tweet import Tweet

class User:

    # Data Members
    username = ""
    tweetList = []

    avgPolarity = 0.0 # This will most likely be from -5 to 5
    avgSubjectivity = 0.0

    ###########################################################
    # Constructor ( should just leave it as a default constructor
    def __init__ (self, username):

       # Set in the data memebers
       self.username = username
       self.tweetList = []


    ###########################################################
    
    def addTweet(self, tweet):

        # Run through the replies and determine each replies polarity
        # Tweets are coming in reverse order
        self.tweetList += [tweet]

            


