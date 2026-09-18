# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData, find_cheapest_flight
from pprint import pprint

import requests_cache
from datetime import datetime, timedelta

requests_cache.install_cache(
    "flight_cache",
    urls_expire_after={
        "*.sheet.co*": requests_cache.DO_NOT_CACHE,
        "*": 3600,
    },
)

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
# pprint(sheet_data)

# --- Get tomorrow and six months from now dates ---
tomorrow = datetime.now() + timedelta(days=1)
six_months_from_now = datetime.now() + timedelta(days=180)

# --- Get Flight Info for London to Paris ---
flight_search = FlightSearch()
flights = flight_search.check_flights("LHR", "CDG", tomorrow, six_months_from_now)

# --- Find the cheapest flight from London to Paris ---
cheapest_flight = find_cheapest_flight(flights, six_months_from_now)
cheapest_flight.print_flightdata()
