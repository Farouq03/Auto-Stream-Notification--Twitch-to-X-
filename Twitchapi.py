import requests
import os

TWITCH_CLIENT_ID = os.getenv('TWITCH_CLIENT_ID')
TWITCH_CLIENT_SECRET = os.getenv('TWITCH_CLIENT_SECRET')
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
}

data = f'client_id={TWITCH_CLIENT_ID}&client_secret={TWITCH_CLIENT_SECRET}&grant_type=client_credentials'

response = requests.post('https://id.twitch.tv/oauth2/token', headers=headers, data=data)
json_data = response.json()
Token = json_data['access_token']
Token_type = json_data['token_type'].capitalize()




