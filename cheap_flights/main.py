# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
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

HOME_AIRPORT_CODE = "SFO"

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
pprint(sheet_data)

# --- Get tomorrow and six months from now dates ---
tomorrow = datetime.now() + timedelta(days=1)
six_months_from_now = datetime.now() + timedelta(days=180)

# --- Get Flight Info for London to Paris ---
flight_search = FlightSearch()
# flights = flight_search.check_flights("LHR", "CDG", tomorrow, six_months_from_now)
# print(flights)
for line in sheet_data["sheet1"]:
    flights = flight_search.check_flights(
        HOME_AIRPORT_CODE, line["iataCode"], tomorrow, six_months_from_now
    )
    # --- Find the cheapest flight from London to Paris ---
    cheapest_flight = find_cheapest_flight(flights, six_months_from_now)
    if cheapest_flight.price < line["lowestPrice"]:
        print(
            f"{line['city']} has a cheaper price than {line['lowestPrice']}: {cheapest_flight.price}"
        )
        data_manager.update_lowest_price(line["id"], cheapest_flight.price)
