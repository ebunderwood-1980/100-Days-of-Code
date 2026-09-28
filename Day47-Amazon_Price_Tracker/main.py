# Imports
from bs4 import BeautifulSoup as BS
import requests
import os
from dotenv import load_dotenv
import smtplib

# Load the .env file values
load_dotenv()

# Variable Declarations
# URL = "https://appbrewery.github.io/instant_pot/"
URL = "https://www.amazon.com/dp/B075CYMYK6?lv=shuf&channelId=751&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&plpRedirect=mhFallback&th=1"
TARGET_PRICE = 100.00
current_price = None
my_email = os.environ["EMAIL_ADDRESS"]
email_smtp = os.environ["SMTP_ADDRESS"]
password = os.environ["EMAIL_PASSWORD"]
amazon_header = {
    "Accept-Language": "en-US",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36}",
}

# Step 1 - Use BeautifulSoup to scrape the product price.
response = requests.get(URL, headers=amazon_header)
amazon_html = response.text

amazon_soup = BS(amazon_html, "html.parser")
current_price = float(
    amazon_soup.find(name="span", class_="aok-offscreen").getText().split("$")[1]
)
print(f"The current price of the crockpot is ${current_price}.")

# Check price against target price and send an email out if current < target.
if current_price < TARGET_PRICE:
    try:
        with smtplib.SMTP(email_smtp, port=587, timeout=10) as connection:
            connection.starttls()

            print("Logging in to Gmail...")
            connection.login(user=my_email, password=password)

            print("Sending email")
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=f"Subject:  Crockpot Price Dropped!\n\nCurrent Price:  ${current_price}".encode(
                    "utf-8"
                ),
            )
            print("Email sent successfully!")
    except TimeoutError:
        print("Connection timed out.  Your internet provider is block port 587")
    except Exception as e:
        print("An Error Occurred: {e}")
