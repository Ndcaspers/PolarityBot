#!/bin/bash

# Obtain commandline arguments
STATUS_ID=$1
BEARER_TOKEN=$2
OUTPUT_JSON=$3

# check the arguments
echo "Status Given: ${STATUS_ID}"
echo "Bearer Token: ${BEARER_TOKEN}"
echo "Output JSON file path: ${OUTPUT_JSON}"

#echo "Bearer Token: $BEAR_TOKEN"
#echo "Currling for Tweets..."
curl -s -X GET \
    -H "Authorization: Bearer ${BEARER_TOKEN}" \
    -H "Content-Type: application/json" \
    "https://api.twitter.com/1.1/statuses/show.json?id=${STATUS_ID}" > $OUTPUT_JSON

# The original tweet id: 936115072551792640
# The reply id: 936115147147563013

