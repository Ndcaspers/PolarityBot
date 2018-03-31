# Nick Caspers
# Dec 29, 2017
#####################################################################################

# StopWatch Class
# Takes in a root tweet and its replies, and determines its polarity

import time

class Stopwatch:

    # Data Members
    startTime = 0
    
    ################################################
    # Constructor (default)

    #################################################
    # Object methods
    def startTime(self):
  
        # Start the stop watch
        self.startTime = time.clock()


    def elapsedTime(self):

        # Get the time elapsed since the startTime
        return time.clock() - self.startTime


