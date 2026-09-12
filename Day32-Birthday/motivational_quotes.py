import datetime as dt
import smtplib
import random as rand

# ---------- Constants and Variables ----------
email = "e.b.underwood@gmail.com"
password = "nvnm pbvq smfy xguq"
quotes = []
motivational_quote = ""
date = None
day_of_the_week = None


# ---------- Main ----------
# Read the motivational quotes into a list.
with open("quotes.txt") as file:
    quotes = file.readlines()

# Check datetime to see if it is time to send a quote.
date = dt.datetime.now()
day_of_the_week = date.weekday()

# Send email with quote if day is Saturdday (day 5)
if day_of_the_week == 5:
    motivational_quote = rand.choice(quotes).strip()

    # Set up email and send off the quote
    with smtplib.SMTP("smtp.gmail.com", port=587, timeout=10) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=email,
            msg=f"Subject:  Weekly motivational quote\n\n{motivational_quote}",
        )
