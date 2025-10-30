# Auto Stream Notification (Twitch to X)
This is simple python code that i use to automatically posts tweets on X when you go live on Twitch. (by using X API and Twitch API)

## Requirements
- Python 3.x
- Twitch Developer Account
- X (Twitter) Developer Account

## Setup
1. Clone this repository:
```bash
git clone https://github.com/Farouq03/Auto-Stream-Notification--Twitch-to-X-.git
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file with your API keys:
```env
# Twitch API
TWITCH_CLIENT_ID=your_twitch_client_id
TWITCH_CLIENT_SECRET=your_twitch_client_secret
YOUR_TWITCH_NAME=your_twitch_username

# X (Twitter) API
api_keys=your_twitter_api_key
api_secret=your_twitter_api_secret
bearer_token=your_twitter_bearer_token
access_token=your_twitter_access_token
access_token_secret=your_twitter_access_token_secret
```
* Note : You can get your API keys by creating Twitch and X developer account and following their guide

## Usage

Run the script:
```bash
python AutoTweetX.py
```

The script will check if you're live on Twitch and automatically post a tweet with your stream title when you go live.

## Project Files
- `AutoTweetX.py` - Main script that handles X (Twitter) posting
- `Twitchapi.py` - Handles Twitch API authentication
- `TwitchInfo.py` - Manages stream status checking
- `requirements.txt` - Lists required Python packages
- `.env` - Stores your API credentials (not included)

## Security Note
⚠️ Never share your `.env` file or API credentials
⚠️ Make sure to add `.env` to your `.gitignore` file