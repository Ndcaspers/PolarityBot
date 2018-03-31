# Nick Caspers
# Dec 1, 2017
#################################

# MyMath class
# Purpose is to determine the standard deviation 

import math

# MyMath class
class MyMath:

    ###########################
    # static methods
    @staticmethod
    def stdDeviationWithAvg(numberList, avg):

        # compute the standard deviation
        listLength = len(numberList)

        # get teh summation for the std deviation
        stdSummation = 0.0

        for i in range(0, listLength):
    
            stdSummation += ((numberList[i] - avg) ** 2)

        # retrn the result
        return (math.sqrt(stdSummation / (listLength - 1)))
