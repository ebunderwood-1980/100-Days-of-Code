import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

SHEETY_PRICES_ENDPOINT = os.environ["SHEETY_ENDPOINT"]
SHEETY_TOKEN = os.environ["TOKEN"]


class DataManager:
    def __init__(self):
        self._authorization = {
            "Authorization": SHEETY_TOKEN,
        }
        self.destination_data = {}

    def get_destination_data(self):
        # 2. Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=self._authorization)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data
        return self.destination_data
