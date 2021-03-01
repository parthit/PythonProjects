
import random
import pandas
import datetime as dt
import smtplib
my_email = "parthittesting@gmail.com"
my_password = "123abc()"

bfile = pandas.read_csv('birthdays.csv').to_dict(orient='records')
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    for person in bfile:
        if (person['month'], person['day']) == (dt.datetime.now().month, dt.datetime.now().day) :
            with open(file=f'letter_templates/letter_{random.randint(1,3)}.txt', mode="r") as letter:
                hbd_letter = letter.read()
                hbd_letter = hbd_letter.replace("[NAME]", person['name'])
                connection.sendmail(from_addr=my_email,
                                    to_addrs=person['email'],
                                    msg=f"Subject:Happy Birthday!\n\n{hbd_letter}\n\n\nSent by Parthit's Python Code")


# Something that was really cool:
# Doing dictionary comprehension
# data = pandas.read_csv("birthdays.csv")
# print(data)
# birthday_dict = { (data_row['month'],data_row['day']):data_row for (index, data_row) in data.iterrows()}
# print(birthday_dict[(3,1)])
