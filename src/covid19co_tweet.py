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
import pytz
import os
import tweepy

# Colombia Covid19 Resume Dataset
covid19co_resume = pd.read_csv(os.path.join('../input', 'covid19co_resume.csv'))

# Data Resume
# ['date', 'total_reported', 'accum_reported', 'total_recovered', 'accum_recovered', 'total_deceased', 'accum_deceased', 'accum_samples']
data_resume = list(covid19co_resume.values[0])
print(data_resume)

# Check Accum Values
if data_resume[2] > 0 and data_resume[4] > 0 and data_resume[6] > 0 and data_resume[7] > 0:
    # Resume Avalaible
    print('Resume avalaible')
    #tz_co = pytz.timezone('America/Bogota')
    #local_dt = datetime.datetime.utcnow() - datetime.timedelta(hours=5)
    #LOCAL_DATETIME = local_dt.astimezone(tz_co).strftime('%Y-%m-%dT%H:%M:%S')
    LOCAL_DATETIME = datetime.datetime.utcnow().astimezone(pytz.timezone('America/Bogota')).isoformat()

    # Text Tweet
    text_tweet = """.:-_-:.
Fecha Reporte: {data[0]}
Casos: {data[1]} ; Accum: {data[2]}
Recuperados: {data[3]} ; Accum: {data[4]}
Fallecidos: {data[5]} ; Accum: {data[6]}
Muestras Accum: {data[7]}
#Colombia #Covid19 #Resumen #Coronavirus #Actualizado
#Datasets https://sebaxtian.github.io/colombia_covid_19_pipe""".format(data=data_resume)

    # Read Last Tweet
    with open('../output/last_tweet', 'r') as last_tweet_file:
        last_tweet = last_tweet_file.read()
        #print('last_tweet:', last_tweet)

    if text_tweet == last_tweet:
        print('No changes, do nothing')
        #print(text_tweet)
    else:
        print('Post Tweet')
        # Write New Tweet
        with open('../output/last_tweet', 'w') as last_tweet_file:
            last_tweet_file.write(text_tweet)
        # Add datetime
        text_tweet += '\nHora Local: {date_time}'.format(date_time=LOCAL_DATETIME)
        # Post Tweet
        # Authentication
        auth = tweepy.OAuthHandler(os.getenv('TWEET_CONSUMER_KEY'), os.getenv('TWEET_CONSUMER_SECRET'))
        auth.set_access_token(os.getenv('TWEET_ACCESS_TOKEN'), os.getenv('TWEET_ACCESS_TOKEN_SECRET'))
        # Tweepy API Object
        api = tweepy.API(auth)
        # Send Tweet
        api.update_status(text_tweet)
        print(text_tweet)
else:
    # Resume Unavalaible
    print('Resume unavalaible')
