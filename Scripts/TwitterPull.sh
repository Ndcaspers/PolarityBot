#!/bin/bash

# Should be some of the attempts in pulling data from Twitter

BEAR_TOKEN="AAAAAAAAAAAAAAAAAAAAAPAh2AAAAAAAoInuXrJ%2BcqfgfR5PlJGnQsOniNY%3Dn9galDg4iUr7KyRAU47JGDbQz2q7sdwXRTkonzBX2uLxXRgNv0"

echo "Bearer Token: $BEAR_TOKEN"
echo "Currling for Tweets..."

curl -X GET \
    -H "Authorization: Bearer $BEAR_TOKEN" \
    -H "Content-Type: application/json" \
    'https://api.twitter.com/1.1/search/tweets.json?q=to:Caspe159&count=100' \
    > ../jsonFiles/tweets.json
#'https://api.twitter.com/1.1/search/tweets.json?q=https://twitter.com/Caspe159/status/900455502261432320&count=100' \

# Display the Tweets via Python
#python ./Main.py

