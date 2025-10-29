import requests
from TwitchInfo import checkUser, getTitle, getUserlogin
from requests_oauthlib import OAuth1
import random
import os

# Load Twitter API credentials from environment variables
api_keys = os.getenv('api_keys')
api_secret = os.getenv('api_secret')
bearer_token = os.getenv('bearer_token')
access_token = os.getenv('access_token')
access_token_secret = os.getenv('access_token_secret')

# Set up OAuth1 authentication
auth = OAuth1(api_keys, api_secret, access_token, access_token_secret)

#check if user is live
status = checkUser()

if status == True:
    #get stream title
    streamtitle = getTitle()
    
    #post tweet
    tweet_data = {"text": f"Im LIVE!!:{streamtitle} streaming now on Twitch! https://twitch.tv/{getUserlogin()}"}

    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json",
    }
    response = requests.post(
        "https://api.twitter.com/2/tweets",
        json=tweet_data,
        auth=auth,
    )
    if response.status_code == 201:
        print("Tweet posted successfully!")
    else:
        print(f"Failed to post tweet: {response.status_code}")
else:
    print("User is not live.")

