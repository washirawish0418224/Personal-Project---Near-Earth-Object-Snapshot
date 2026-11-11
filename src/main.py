import requests
import os 
import pandas as pd
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
feed_dict = feed_req.json()
feed_df = pd.DataFrame.from_dict(
    data = feed_dict
)

#extracting three components
pagination_link = feed_dict['links']
element_count = feed_dict['element_count']
neo_data = feed_dict['near_earth_objects']

#data wrangling
neo_list = []
for date in neo_data.items():
    for asteroid in date[1]:
        asteroid['date'] = date[0]
        neo_list.append(asteroid)

neo_df_nor= pd.json_normalize(neo_list)
neo_df_nor_exp = pd.json_normalize(neo_df_nor['close_approach_data'].explode()).add_prefix('cad.')
neo_df = pd.concat([neo_df_nor.drop(columns='close_approach_data'), neo_df_nor_exp], axis = 1)
breakpoint()