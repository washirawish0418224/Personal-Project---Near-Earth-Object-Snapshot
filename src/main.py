import requests
import os 
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
api_key = os.getenv('NASA_API_KEY')
now = datetime.now()

#example: https://api.nasa.gov/neo/rest/v1/feed?start_date=START_DATE&end_date=END_DATE&api_key=API_KEY
url_feed = 'https://api.nasa.gov/neo/rest/v1/feed'
url_lookup = 'https://api.nasa.gov/neo/rest/v1/neo/'
param_feed = {
    'start_date': now,
    'end_date':None,
    'api_key':api_key
}

param_lookup = {
    'asteroid_id': None,
    'api_key': api_key
}

feed_req = requests.get(url_feed, params=param_feed)
breakpoint()