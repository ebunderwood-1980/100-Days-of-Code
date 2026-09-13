import smtplib
import datetime as dt
import pandas
import random as rand

# ---------- Constants and Variables ----------
EMAIL = "e.b.underwood@gmail.com"
PASSWORD = "nvnm pbvq smfy xguq"
recipient_list = None
letters_location = [
    "./letter_templates/letter_1.txt",
    "./letter_templates/letter_2.txt",
    "./letter_templates/letter_3.txt",
]
letters = []
letter_bodies = []

# ---------- Main ----------

# Get todays month and day
today_month = dt.datetime.now().month
today_day = dt.datetime.now().day

# Read in people from CSV and check list for birthdays
birthday_df = pandas.read_csv("birthdays.csv")
birthday_dict = birthday_df.to_dict(orient="records")
birthday_list = [
    person
    for person in birthday_dict
    if person["month"] == today_month and person["day"] == today_day
]

# Read in all of the birthday letters into a list
for file in letters_location:
    with open(file, "r") as f:
        letters.append(f.read())

# Pick a random letter to send out
letter_to_send = rand.choice(letters)

# Go through each of the birthday folks and create a separate letter
for person in birthday_list:
    person_name = person["name"]
    person_email = person["email"]
    new_letter = letter_to_send.replace("[NAME]", person_name)

    # Mail the letter to each birthday person
    with smtplib.SMTP("smtp.gmail.com", port=587, timeout=10) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=person_email,
            msg=f"Subject: Happy Birthday\n\n{new_letter}",
        )
