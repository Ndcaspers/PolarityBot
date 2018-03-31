import sys
import os
import json

# Checking the Shell Command Running
#(Note the program waits for the shell command to returns
print("Ya nothing... BUT TRASH!!!")
os.system('echo "Hype Man 1: Yeah! Get\'em!"')

# Testing the json parser
#Read a JSON file into one string
#jsonFile = open("./QuotedTweet.json", 'r')
#jsonFile = open("./QuotedTweet.json", 'r')
jsonFile = open(sys.argv[1], 'r')
#jsonData = jsonFile.read()
#jsonFile.close()

print("Displaying JSON Data ( " + jsonFile.name + " )...")

# Apparently load straight file into json ( For json.load anyways )
#if you use json.loads should work just as well
#parsedJson = json.load(open("./QuotedTweet.json", 'r'))
parsedJson = json.load(open(sys.argv[1], 'r'))
#print("Displaying JSON Data ( " + jsonFile.name + " )...")
print( json.dumps(parsedJson, indent=2) )

