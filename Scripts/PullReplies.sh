#!/bin/bash

# Need to check arguments
ACCOUNT="$1"
MAX_ID="$2"
SINCE_ID="$3"
BEARER_TOKEN="$4"
OUTPUT_JSON="$5"

# Check the arguments given
echo "Account Name: ${ACCOUNT}"
echo "max_id: ${MAX_ID}"
echo "since_id: ${SINCE_ID}"
echo "Bearer Token: ${BEARER_TOKEN}"
echo "Output JSON Path: ${OUTPUT_JSON}"

# cURL in the tweets
QUERY="empty"

if [ "${MAX_ID}" == "-1" ]
then
    # No max_id, send a request without it
    QUERY="https://api.twitter.com/1.1/search/tweets.json?q=to:${ACCOUNT}&since_id=${SINCE_ID}&count=100"
else
    # max_id found, add it to the request
    QUERY="https://api.twitter.com/1.1/search/tweets.json?q=to:${ACCOUNT}&max_id=${MAX_ID}&since_id=${SINCE_ID}&count=100"
fi

# Actually send the pull
curl -s -X GET \
    -H "Authorization: Bearer ${BEARER_TOKEN}" \
    -H "Content-Type: application/json" \
    "${QUERY}" \
    > $OUTPUT_JSON

