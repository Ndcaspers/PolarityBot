# Nick Caspers
# Dec 14, 2017
#####################################################################################

# TweetAnalyzer Class
# When provided a root tweet and its replies, the class will determine the root tweet's polarity

# Library used for sentiment analysis
from textblob import TextBlob 

# created classes
from Config import Config
from Tweet import Tweet
from User import User
from MyMath import MyMath


class TweetAnalyzer:

    # Data Members
    entryNum = -1
    rootTweet = None
    replyTweetList = []

    userList = []

    retweetCount = 0
    favoriteCount = 0

    avgPolarity = 0.0 # These will most likely be from -5 to 5
    avgSubjectivity = 0.0
    stdPolarity = 0.0
    stdSubjectivity = 0.0

    percentPos = -1.0
    percentNeg = -1.0
    percentNeut = -1.0

    wordFreqPairs = []
    highFreqAmount = 3 # change to determine the depth of the high freq
    highWordFreq = []

    hashTagFreq = []
    highHashFreq = ["", -1]

    ###########################################################
    # Constructor 
    def __init__ (self, rootTweet, replyTweetList):

        # Determine the entry number
        self.entryNum = self.latestEntryNum() + 1

        # Set in the data memebers
        self.rootTweet = rootTweet
        self.retweetCount = rootTweet.retweetCount
        self.favoriteCount = rootTweet.favoriteCount
        self.replyTweetList = replyTweetList

        # determine the amount of high freq words wanted (usually 3)
        for i in range(0, self.highFreqAmount):
            self.highWordFreq += [["", -1]]


    ###########################################################
    # Statistic Gathering Methods
    def compilePolarity(self):

        # analyze the replies to the root tweet
        self.analyzeReplies()

        # run through the users and average out their tweets polarity
        self.compileUserPolarity()

        # average out the polaritys of all the users
        self.calcAvgUserPolarity()

        # Determine the std deviation
        self.calcStdDeviation()

        # compute the percent of pos neg and neutral
        self.calcPercents()


    def compileWordFreq(self):

        # prepare the list of words and frequency sets
        self.getWordFreq()

        # determine the higher freq of the set
        self.getHighWordFreq()

        # determine the highest hash tag frequency
        self.getHighHashTag()


    ################################################################
    # compilePolarity() Helper Methods
    def analyzeReplies(self):

        print("Analyzing Replies...")
        print("Sorting Out the Tweets to Users...")

        # Create List of users
        # Run through the replies and sort into the various users
        for i in range(0, len(self.replyTweetList)):

            tweet = self.replyTweetList[i]
            self.addNameList(tweet.userName, tweet)

        print(" ")
        print("Finding Polarity Values of Tweets...")

        # Root Tweet first
        print("Root Tweets...")
        self.findPolarity(self.rootTweet)

        # Reply Tweets Next
        print("Reply Tweets...")

        # Run through the various profiles, determining the polarity towards the root tweet
        for i in range(0, len(self.userList)):
        
            for j in range(0, len(self.userList[i].tweetList)):
            
                # Check the current tweet
                self.findPolarity(self.userList[i].tweetList[j])


    def findPolarity(self, tweet):
        
        # Use the textblob and find the polarity vs objectivity scores
        # Note multiply by 5 to spread out the polarity
        multiplier = 5.0

        tweetTextBlob = TextBlob(tweet.text)
        tweet.setPolarityValues(multiplier * tweetTextBlob.sentiment.polarity, multiplier * tweetTextBlob.sentiment.subjectivity)
        

    def compileUserPolarity(self):

        # Run through the users and determine the polarity of each user
        for i in range(0, len(self.userList)):

            # Prepare for average calculations
            currentPolaritySum = 0.0
            currentSubjectivitySum = 0.0

            zeroPolarityCounter = 0
            zeroSubjectivityCounter = 0

            tweetAmount = len(self.userList[i].tweetList)
            
            # Run through the tweets and find the average polarity and subjectivity
            for j in range(0, tweetAmount): 
            
                # Accumulate accounts keeping in mind the amount of zeros
                currentPolaritySum += self.userList[i].tweetList[j].polarity
                currentSubjectivitySum += self.userList[i].tweetList[j].subjectivity

                if(self.userList[i].tweetList[j].polarity == 0):
                    zeroPolarityCounter += 1
                if(self.userList[i].tweetList[j].subjectivity == 0):
                    zeroSubjectivityCounter += 1

            # Compute the average taking into account the amount of zeros
            avgPolarity = 0.0
            avgSubjectivity = 0.0

            if(zeroPolarityCounter != tweetAmount):
                avgPolarity = currentPolaritySum / (tweetAmount - zeroPolarityCounter)
            
            if(zeroSubjectivityCounter != tweetAmount):
                avgSubjectivity = currentSubjectivitySum / (tweetAmount - zeroSubjectivityCounter)

            # Store the averages into the user variables
            self.userList[i].avgPolarity = avgPolarity
            self.userList[i].avgSubjectivity = avgSubjectivity


    def calcAvgUserPolarity(self):
    
        # Run through the users and average the polarity and subjectivity
        polaritySum = 0.0
        subjectivitySum = 0.0

        zeroPolarityCount = 0
        zeroSubjectivityCount = 0

        userAmount = len(self.userList)

        for i in range(0, userAmount):

            polaritySum += self.userList[i].avgPolarity
            subjectivitySum += self.userList[i].avgSubjectivity

            if(self.userList[i].avgPolarity == 0.0):
                zeroPolarityCount += 1
            if(self.userList[i].avgSubjectivity == 0.0):
                zeroSubjectivityCount +=1

        # Compute the average polarity and subjectivity
        avgPolarity = 0.0
        avgSubjectivity = 0.0
   
        if(zeroPolarityCount != userAmount):
            avgPolarity = polaritySum / (userAmount - zeroPolarityCount)
        if(zeroSubjectivityCount != userAmount):
            avgSubjectivity = subjectivitySum / (userAmount - zeroSubjectivityCount)
        
        self.avgPolarity = avgPolarity
        self.avgSubjectivity = avgSubjectivity

        
    def calcStdDeviation(self):

        # determine the polarity std deviation of the users
        userPolarityList = []
        userSubjectivityList = []

        for i in range(0, len(self.userList)):

            userPolarityList += [self.userList[i].avgPolarity + 5.0]
            userSubjectivityList += [self.userList[i].avgSubjectivity + 5.0]

        # Send data off to be computed and set std
        self.stdPolarity = MyMath.stdDeviationWithAvg(userPolarityList, self.avgPolarity + 5.0)
        self.stdSubjectivity = MyMath.stdDeviationWithAvg(userSubjectivityList, self.avgSubjectivity + 5.0)


    def calcPercents(self):

        # run through the user polarities and determine amount in each category
        numPos = 0
        numNeg = 0
        numNeut = 0
        totalUsers = len(self.userList)

        for i in range(0, totalUsers):

            userAvgPolarity = self.userList[i].avgPolarity
            #print("userAvgPolarity: " + str(userAvgPolarity))

            if(userAvgPolarity >= (0.01 / 5)):
                numPos += 1

            elif(userAvgPolarity <= (-0.01 / 5)):
                numNeg += 1

            else:
                numNeut += 1

        # set the percentage values
        self.percentPos = float(numPos) / float(totalUsers)
        self.percentNeg = float(numNeg) / float(totalUsers)
        self.percentNeut = float(numNeut) / float(totalUsers)

    ###########################################################
    # compileWordFreq() Helper Methods
    def getWordFreq(self):

        # Run through the users
        for i in range(0, len(self.userList)):

            #print("Checking User: " + self.userList[i].username)

            # Run through each tweet of each user
            for j in range(0, len(self.userList[i].tweetList)):

                # split apart the tweet text and run through each word, ignoring capitalization
                textWordList = self.userList[i].tweetList[j].text.split(" ")
                wordListLength = len(textWordList)

                for k in range(0, wordListLength):

                    # remove punctuation
                    modWord = self.removePunctuation(textWordList[k])

                    # could be empty tweet
                    if(modWord == ""):
                        continue

                    # determine if it belongs in the hash tags
                    self.checkHashTag(modWord)

                    # check if the word is already in the freqeuncy list
                    indexInFreq = self.wordInFreqList(modWord)

                    if(indexInFreq != -1):
                        #It is
                        self.wordFreqPairs[indexInFreq][1] += 1
                    else:
                        # It isnt
                        self.wordFreqPairs += [[modWord, 1]]

    def getHighWordFreq(self):

        # determine words with high frequencies that matter
        # Might want to add to this list later on...
        unimpWords = ["of",  "the", "are", "is", "be", "to", "there", "and", "your", "you're", "their", "in", "down", "up", "go", "with", "have", "has", "had", "being", "was", "were", "cant", "dont", "doesnt", "wasnt", "coudnt", "wouldnt", "could", "would", "does", "I", "you", "a", "an", "for", "it", "from", "that", "this", "on", "about", "not", "we", "so", "he", "they"]

        # Added words due to nature of replies
        unimpWords += ["@" + self.rootTweet.userName]

        # filter out the unimportant words
        impWordFreq = []
        unimpFlag = False
        
        for i in range(0, len(self.wordFreqPairs)):

            unimpFlag = False

            for j in range(0, len(unimpWords)):

                if(unimpWords[j].lower() == self.wordFreqPairs[i][0].lower()):
                    unimpFlag = True

            if(not(unimpFlag)):
                impWordFreq += [[self.wordFreqPairs[i][0], self.wordFreqPairs[i][1]]]

        # Determine the three highest word frequencies
        for i in range(0, len(impWordFreq)):

            tempPair = impWordFreq[i]

            for j in range(0, len(self.highWordFreq)):

                # determine ir the freqeuncy is higher than the already established
                if(self.highWordFreq[j][1] < tempPair[1]):

                    # store the original high word and freq, to be placed in the temp
                    originalHighWord = self.highWordFreq[j][0]
                    originalHighFreq = self.highWordFreq[j][1]

                    self.highWordFreq[j][0] = tempPair[0]
                    self.highWordFreq[j][1] = tempPair[1]

                    tempPair[0] = originalHighWord
                    tempPair[1] = originalHighFreq


    def getHighHashTag(self):

        # just run through the frequency list and obtain the highest freq
        highFreqIndex = -1
        highFreq = -1

        for i in range(0, len(self.hashTagFreq)):

            #print("HashTag: " + self.hashTagFreq[i][0] + " , " + str(self.hashTagFreq[i][1]))

            if(self.hashTagFreq[i][1] > highFreq):
    
                highFreqIndex = i
                highFreq = self.hashTagFreq[i][1]

        if(len(self.hashTagFreq) != 0):
            self.highHashFreq = [self.hashTagFreq[highFreqIndex][0], highFreq]
            print(self.highHashFreq)



    ###########################################################
    # Generic Helper Methods
    def addNameList(self, givenName, tweet):

        # determine if the given name is in the list
        breakFlag = False

        for i in range(0, len(self.userList)):

            # User found, add the tweet to the user and return
            if(self.userList[i].username == givenName):

                self.userList[i].tweetList += [tweet]
                return

        # User not in the list, append name and add tweet to new user
        self.userList += [User(givenName)]
        self.userList[-1].tweetList += [tweet]

    
    def wordInFreqList(self, word):

        # Determine if the word is in the frequency list and return the index
        keyIndex = -1
        modifiedWord = word.lower()

        if(word == ""):
            return keyIndex

        for i in range(0, len(self.wordFreqPairs)):

            # word is found, return the index
            if(self.wordFreqPairs[i][0].lower() == modifiedWord):
                keyIndex = i
                return keyIndex

        return keyIndex


    def removePunctuation(self, word):

        # determine if its a link
        newWord = ""
        linkFlag = len(word) > 4

        if(linkFlag):
            linkFlag = (word[:4] == "http")

        if(linkFlag):
            # it is a link, therefore, just ship it back
            newWord = word

        else:
            # remove the punctuation in a word
            punctuation = ",\"?!().:;'-"
            newWord = word.translate(None, punctuation)

        return newWord


    def checkHashTag(self, word):

        # determine if should add word to the hashtag list
        if(word[0] != "#"):
            return

        # run through and check if it already exists in the hashtag list
        for i in range(0, len(self.hashTagFreq)):

            if(self.hashTagFreq[i][0] == word):

                self.hashTagFreq[i][1] += 1
                return

        # have yet to come across this specific hash tag
        self.hashTagFreq += [[word, 1]]


    def latestEntryNum(self):

        # open up the log file
        logFile = open(Config.logPath, 'r')

        # run through i tand determine the lastest entry
        currentLine = ""
        currentLine = logFile.readline()

        splitLine = []
        maxEntry = 0

        while(currentLine):

            # determine if worth breaking apart
            splitLine = currentLine.split(' ')
    
            if(len(splitLine) != 2):

                currentLine = logFile.readline()
                continue

            elif(splitLine[0] == "Entry:"):

                # It is an entry, take the number
                entryNumStr = splitLine[1].translate(None, "\n")
                entryNum = int(entryNumStr)

                if(entryNum > maxEntry):
                    maxEntry = entryNum

            # read in the next line
            currentLine = logFile.readline()

        # close the open file and return the max Entry
        logFile.close()

        return maxEntry

            
    ####################################################################
    #toString mehtods
    def toStringHighWordFreq(self):
   
        # provide a string for the high frequency words
        highFreqString = ""

        for i in range(0, len(self.highWordFreq)):

            if(self.highWordFreq[i][0] != "" and self.highWordFreq[i][1] > 10):

                highFreqString += str(i + 1) + "st Word: " + self.highWordFreq[i][0] + "(Freq: " + str(self.highWordFreq[i][1]) + ")\n"

        return highFreqString


    # the responses
    def toStringSentiment(self):

        # the update including the sentiment portion of the analysis
        # construct the update
        sentiment = "(1/2) Daily Tweet Analysis #" + str(self.entryNum) + " \n"

        if(round(self.avgPolarity, 2) > 0.0):
            sentiment += "\nUser Sentiment (+5.0 to -5.0): +" + str(round(self.avgPolarity, 2))

        elif(round(self.avgPolarity, 2) == 0.0 or round(self.avgPolarity, 2) == -0.0):
            sentiment += "\nUser Sentiment (+5.0 to -5.0): 0.0"
    
        else:
            sentiment += "\nUser Sentiment (+5.0 to -5.0): " + str(round(self.avgPolarity, 2))


        sentiment += "\nStandard Deviation: " + str(round(self.stdPolarity, 2)) + "\n"
        sentiment += "Sentiment Spread: " + str(round(self.percentPos, 2) * 100) + "% Positive - " + str(round(self.percentNeut, 2) * 100) + "% Neutral - " + str(100 - (100 * (round(self.percentPos, 2) + round(self.percentNeut, 2)))) + "% Negative\n"

        # quote in the tweet
        #sentiment += self.rootTweet.getLink()

        return sentiment


    def toStringFreq(self):

        # The second part of the response tailoring to the freqeuncy of words
        freq = "(2/2) Most frequently used (notable) words in direct replies:\n\n"

        # add in the words
        for i in range(0, len(self.highWordFreq)):

            freq += self.highWordFreq[i][0] + " (" + str(self.highWordFreq[i][1]) + ")\n"

        # if there is a high freq hash tag add that in
        if(self.highHashFreq[1] > 5):

            freq += "\nMost frequently used hashtag: " + self.highHashFreq[0] + " (" + str(self.highHashFreq[1]) + ")\n"

        return freq

    def toStringUpdate(self):

        # with the statistics in the replies send notice of new tweet analysis
        #entryAmount = self.latestEntryNum()
        noticeUpdate = "Daily Tweet Analysis #" + str(self.entryNum) + ", featuring @" + self.rootTweet.userName + " \n\n"
	noticeUpdate += self.rootTweet.getLink()

        return noticeUpdate


    def toStringSentimentReply(self):

        # Create the reply for sentiment
        sentimentReply = "@" + self.rootTweet.userName + " " + self.toStringSentiment()

        return sentimentReply


    def toStringFreqReply(self):

        # create reply for freqeuency
        frequencyReply = "@" + self.rootTweet.userName + " " + self.toStringFreq()

        return frequencyReply


    def toStringReply(self):

        # Create a  reply to the origianl tweet
        reply = "@" + self.rootTweet.userName + " check out other statistics here @PolarityBot"

        return reply


    def toString(self):

        # the generic toString for the whole class
        analysisString = ""

        analysisString += "RootTweetID: " + str(self.rootTweet.tweetID) + "\n"
        analysisString += "\tAverage Polarity: " + str(self.avgPolarity) + " (std: " + str(self.stdPolarity) + ")" + "\n"
        analysisString += "\tAverage Subjectivity: " + str(self.avgSubjectivity) + " (std: " + str(self.stdSubjectivity) + ")" + "\n"
        analysisString += "\tHigh Word Frequency: " + self.toStringHighWordFreq()

        return analysisString

    

