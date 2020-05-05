#!/bin/bash

#
# Run covid19co_tweet.py Python script
#

# Local .env
if [ -f .env ]; then
    # Load Environment Variables
    export $(cat .env | grep -v '#' | awk '/=/ {print $1}')
    # For instance
    #echo $KAGGLE_KEY
fi

# Download Kaggle Dataset
if [ $KAGGLE_KEY ] && [ $KAGGLE_USERNAME ]; then
    kaggle datasets download -d sebaxtian/covid19co -p ./kaggle --unzip
fi

echo "Work in progress ..."
