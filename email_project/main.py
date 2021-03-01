import smtplib
import random

my_email = "parthittesting@gmail.com"
my_password = "123abc()"



import datetime as dt
day_of_week = dt.datetime.now().weekday()
print(day_of_week)
with open(file="quotes.txt") as file:
    quotes = file.readlines()
    if dt.datetime.now().weekday() == 0:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="ria08.dhanani@gmail.com",
                                msg=f"Subject:Monday Motivation\n\n{random.choice(quotes)}\nSent from Python")
