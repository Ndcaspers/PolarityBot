#!/bin/bash

# Should be some of the attempts in pulling data from Twitter

BEAR_TOKEN="AAAAAAAAAAAAAAAAAAAAAPAh2AAAAAAAoInuXrJ%2BcqfgfR5PlJGnQsOniNY%3Dn9galDg4iUr7KyRAU47JGDbQz2q7sdwXRTkonzBX2uLxXRgNv0"

echo "Bearer Token: $BEAR_TOKEN"
echo "Currling for Tweets..."

curl -X GET \
    -H "Authorization: Bearer $BEAR_TOKEN" \
    -H "Content-Type: application/json" \
    'https://api.twitter.com/1.1/statuses/show.json?id=936115147147563013' \
     > ../jsonFiles/QuotedTweet.json

# The original tweet id: 936115072551792640
# The reply id: 936115147147563013
# Tweet with quote id: 900455573132636160
#&include_ext_alt_text=true
#&include_entities=true


# Display the Tweet info via python
#python ./Main.py

#echo "Displaying Tweet Info..."
