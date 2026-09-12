# ---------- Email and Managing Dates ----------

# Email SMTP and Datetime
# Preloaded Python modules

# Python Mail Google Password:  nvnm pbvq smfy xguq

import datetime as dt

now = dt.datetime.now()  # Gets you the current date and time in a large string
year = now.year  #  Can also use minute, second, day, etc.
month = now.month
day_of_week = now.weekday()

if year == 2026:
    print("It is 2026")

date_of_birth = dt.datetime(
    year=1980, month=9, day=25
)  # Can also use hour, minute, second, etc.
