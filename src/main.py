import requests import os from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('NASA_API_KEY')
