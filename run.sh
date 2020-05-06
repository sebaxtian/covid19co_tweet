#!/bin/bash

#
# Run covid19co_resume.py Python script
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
    #echo ''
    kaggle datasets download -d sebaxtian/covid19co -p ./kaggle --unzip
fi

# Run Colombia Covid19 Resume
cd ./src
python3 covid19co_resume.py
# Run Colombia Covid19 Tweet
python3 covid19co_tweet.py
cd ..

echo "Finish!"
