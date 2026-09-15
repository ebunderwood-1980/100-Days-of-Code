# ------------- API Authentication -------------
# Allows us to use API's for data that is not provided for free.

# API Keys
# Like your own user name and password to get protected API data.  Allows API providers to check how much data you are using.

# ---------- Hiding Environmental Variables ----------
# Examples of Environmental Variables are Auth Tokens, user names, passwords, private data
# Exist for convenience and security.
# from terminal prompt:  export <name>=value
# in python program:  os.environ.get("<varialbe name>")   Must import os


import requests
from twilio.rest import Client

bring_umbrella = False

api_key = "b9b042385c2a6d673b0d83b1e3562031"
latitude = 38.5810606
longitude = -121.493895
endpoint = "https://api.openweathermap.org/data/2.5/forecast"
twilio_sid = "AC8c841fdf8022b461e12e28d8760fa298"
twilio_token = "78818553cf82eb0756bfa0d65f5127c4"

parameters = {
    "lat": latitude,
    "lon": longitude,
    "appid": api_key,
    "units": "imperial",
    "cnt": 4,
}

response = requests.get(url=endpoint, params=parameters)
response.raise_for_status()

sacramento_weather_data = response.json()

weather_codes = [
    (items["dt_txt"], items["weather"][0]["id"])
    for items in sacramento_weather_data["list"]
]
print(weather_codes)
print(sacramento_weather_data["list"][0]["dt_txt"])

for date, code in weather_codes:
    if code <= 1000:
        bring_umbrella = True

if bring_umbrella:
    twilio_client = Client(twilio_sid, twilio_token)
    message = twilio_client.messages.create(
        to="+13476336735",
        from_="+17372583742",
        body="sms_event_notifications",
    )

    print(message.status)

    # You can use PythonAnywhere.com to run a python program on a daily schedule.
