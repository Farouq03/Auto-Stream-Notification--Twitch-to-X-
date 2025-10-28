import requests
import json
import os
from Twitchapi import TWITCH_CLIENT_ID, Token_type, Token, TWITCH_CLIENT_SECRET

YOUR_TWITCH_NAME = os.getenv('YOUR_TWITCH_NAME')


headers = {
    'Authorization': f'{Token_type} {Token}',
    'Client-Id': f'{TWITCH_CLIENT_ID}',
}

params = {
    'user_login': [
        f'{YOUR_TWITCH_NAME}'
    ],
}

response = requests.get('https://api.twitch.tv/helix/streams', params=params, headers=headers)
jsondata = response.json()
print (jsondata)


def checkUser():
    try :
        if 'data' in jsondata:
            if jsondata["data"][0]["type"] != "":
                return True
            else:
                return False
    
    except Exception as e:
        return False

def getTitle():
    try:
        if 'data' in jsondata:
            if jsondata["data"][0]["type"] != "":
               streamtitle = jsondata["data"][0]["title"]
               return streamtitle
    except:
        return False 