import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.environ["SERP_KEY"]
GOOGLE_ENDPOINT = "https://serpapi.com/search"


class FlightSearch:
    def __init__(self):
        self._api_key = API_KEY
        self.flight_info = {}

    def check_flights(self, origin_city, destination_city, from_date, to_date):
        flight_parameters = {
            "engine": "google_flights",
            "departure_id": origin_city,
            "arrival_id": destination_city,
            "outbound_date": from_date.strftime("%Y-%m-%d"),
            "return_date": to_date.strftime("%Y-%m-%d"),
            "type": 1,  # Round trip
            "adults": 1,
            "currency": "USD",
            "api_key": self._api_key,
        }
        response = requests.get(url=GOOGLE_ENDPOINT, params=flight_parameters)
        response.raise_for_status()
        data = response.json()
        self.flight_info = data
        return self.flight_info
