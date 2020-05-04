# Dotenv
from dotenv import load_dotenv
# Environment Variables
from pathlib import Path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

import os
import tweepy

# Authentication
auth = tweepy.OAuthHandler(os.getenv('TWEET_CONSUMER_KEY'), os.getenv('TWEET_CONSUMER_SECRET'))
auth.set_access_token(os.getenv('TWEET_ACCESS_TOKEN'), os.getenv('TWEET_ACCESS_TOKEN_SECRET'))
# Tweepy API Object
api = tweepy.API(auth)
# Send Tweet
api.update_status('.:-_-:. Hello, #Tweepy ...')
