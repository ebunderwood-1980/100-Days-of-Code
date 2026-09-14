# --------- API's (Application Programming Interfaces)----------
# Allows you to get data or interacting with external systems.  An interface between your program and a website.
# Similar to a menu at a resteraunt - lets you know of the things you can do to interrace with an external system.

# API Endpoint - The location of the data on a website (usually a website).
# API Request - Similar to going to the bank to take out money and speaking with a bank teller to get money/information.

import requests
from datetime import datetime as dt

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()  # Raises an exception if there is an issue getting the data.
print(response)  # Prints out the response code.

data = response.json()  # Returns the json dictionary
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
print(f"Long:  {longitude}, Lat:  {latitude}")

# Response Codes - Tell you weather or not your request succeeded or failed.
# 100 - Hold on
# 200 - Here you go
# 300 - Go away
# 400 - You screwed up
# 500 - Website scrwed up

parameters = {
    "lat": 38.6631731,
    "lng": -121.332538,
    "formatted": 0,
}

response_sun = requests.get(
    url="https://api.sunrise-sunset.org/json", params=parameters
)
response_sun.raise_for_status()

data_sun = response_sun.json()
sunrise = data_sun["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data_sun["results"]["sunset"].split("T")[1].split(":")[0]


print(f"Sunrise hour is {sunrise}, Sunset hour is {sunset}.")

time_now = dt.now()

print(time_now.hour)
