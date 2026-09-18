import os
from dotenv import load_dotenv
import requests
from datetime import datetime

load_dotenv()  # Load up my .env values

# --- Constants ---
WEIGHT = 190.5
HEIGHT = 130
AGE = 46
GENDER = "male"

# ---Assign .env values---
id = os.environ["APP_ID"]
key = os.environ["API_KEY"]
sheet_endpoint = os.environ["SHEET_ENDPOINT"]
token = os.environ["TOKEN"]

# ---Nutrition header and endpoint for API request
nutrition_header = {
    "x-app-id": id,
    "x-app-key": key,
}
NUTRITION_ENDPOINT = "https://app.100daysofpython.dev"

# ---Get Exercise Info from User---
while True:
    exercise = input("Tell me which exercise you did:  ").strip().lower()
    if exercise == "done":
        break
    else:
        exercise_request = {
            "query": exercise,
            "weight_kg": WEIGHT,
            "height_cm": HEIGHT,
            "age": AGE,
            "gender": GENDER,
        }

        nutrition_response = requests.post(
            url=f"{NUTRITION_ENDPOINT}/v1/nutrition/natural/exercise",
            json=exercise_request,
            headers=nutrition_header,
        ).json()

        # --- Populate your spreadsheet with your nutrition results ---
        date = datetime.now().strftime("%d/%m/%Y")
        time = datetime.now().strftime("%H:%M:%S")
        exercise = nutrition_response["exercises"][0]["name"].title()
        duration = nutrition_response["exercises"][0]["duration_min"]
        calories = nutrition_response["exercises"][0]["nf_calories"]

        sheety_body = {
            "workout": {
                "date": date,
                "time": time,
                "exercise": exercise,
                "duration": duration,
                "calories": calories,
            }
        }

        sheety_header = {
            "Authorization": token,
        }
        sheety_response = requests.post(
            url=sheet_endpoint, json=sheety_body, headers=sheety_header
        )
