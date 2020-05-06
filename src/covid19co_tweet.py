# Dotenv
from dotenv import load_dotenv
# Environment Variables
from pathlib import Path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# Dependencies
import numpy as np
import pandas as pd
import datetime
import os
import tweepy

# Colombia Covid19 Resume Dataset
covid19co_resume = pd.read_csv(os.path.join('../input', 'covid19co_resume.csv'))

# Datetime
date_time = datetime.datetime.now().isoformat()

# Text Tweet
text_tweet = """.:-_-:.
Fecha Reporte: {data[0]}
Casos: {data[1]} ; Accum: {data[2]}
Recuperados: {data[3]} ; Accum: {data[4]}
Fallecidos: {data[5]} ; Accum: {data[6]}
Muestras Accum: {data[7]}
#Colombia #Covid19 #Resumen""".format(data=list(covid19co_resume.values[0]))

# Read Last Tweet
with open('../output/last_tweet', 'r') as last_tweet_file:
    last_tweet = last_tweet_file.read()
    #print('last_tweet:', last_tweet)

if text_tweet == last_tweet:
    print('No changes, do nothing')
    print(text_tweet)
else:
    print('Post Tweet')
    # Write New Tweet
    with open('../output/last_tweet', 'w') as last_tweet_file:
        last_tweet_file.write(text_tweet)
    # Add datetime
    text_tweet += '\n#Actualizado: {date_time}'.format(date_time=date_time)
    # Post Tweet
    # Authentication
    auth = tweepy.OAuthHandler(os.getenv('TWEET_CONSUMER_KEY'), os.getenv('TWEET_CONSUMER_SECRET'))
    auth.set_access_token(os.getenv('TWEET_ACCESS_TOKEN'), os.getenv('TWEET_ACCESS_TOKEN_SECRET'))
    # Tweepy API Object
    api = tweepy.API(auth)
    # Send Tweet
    api.update_status(text_tweet)
    print(text_tweet)
