import os
from dotenv import load_dotenv

load_dotenv()

id = os.environ["APP_ID"]
key = os.environ["API_KEY"]
sheet_endpoint = os.environ["SHEET_ENDPOINT"]
username = os.environ["USERNAME"]
password = os.environ["PASSWORD"]
token = os.environ["TOKEN"]
