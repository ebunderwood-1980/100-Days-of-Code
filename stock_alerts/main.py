import os
from dotenv import load_dotenv
import requests
from datetime import date, timedelta
import smtplib

load_dotenv()  # Load Environment Variables from .env
THRESHOLD = 1
# TODO Send news via email


def tesla_movement():

    alpha_key = os.environ.get("ALPHA_API")
    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": "TSLA",
        "outputsize": "compact",
        "apikey": alpha_key,
    }
    today = date.today()
    yesterday = today - timedelta(days=1)
    two_days_ago = today - timedelta(days=2)

    response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
    response.raise_for_status()

    tesla_stock_data = response.json()
    two_days_ago_close = float(
        tesla_stock_data["Time Series (Daily)"][str(two_days_ago)]["4. close"]
    )
    yesterday_close = float(
        tesla_stock_data["Time Series (Daily)"][str(yesterday)]["4. close"]
    )
    delta = round(two_days_ago_close - yesterday_close, 2) * -1
    percentage = round(delta / yesterday_close, 2) * 100

    # print(f"48 Hour Close: {two_days_ago_close}")
    # print(f"Yesterday Close: {yesterday_close}")
    # print(f"Delta: {delta}, Percentage:  {percentage}%")

    return percentage


def get_news():
    news_key = os.environ.get("NEWS_API")
    endpoint = "https://newsapi.org/v2/top-headlines"
    parameters = {
        "apiKey": news_key,
        "totalResults": 3,
        "q": "Tesla",
    }

    response = requests.get(url=endpoint, params=parameters)
    response.raise_for_status()

    tesla_news = response.json()

    articles = [(item["title"], item["url"]) for item in tesla_news["articles"]]
    return articles


def send_email_update(percentage, articles):
    email = os.environ.get("EMAIL")
    password = os.environ.get("PASSWORD")

    if percentage < THRESHOLD:
        direction = "up"
    else:
        direction = "down"

    with smtplib.SMTP("smtp.gmail.com", port=587, timeout=10) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=email,
            msg=f"Subject:  Tesla Stonks\n\n{articles}",
        )


movement = tesla_movement()
if (movement >= THRESHOLD) or (movement <= (-1 * THRESHOLD)):
    print("We're going to need to send out an email here")
    articles = get_news()
    send_email_update(movement, articles)
