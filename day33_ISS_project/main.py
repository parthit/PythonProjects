import requests
from datetime import datetime
import smtplib
import time

EMAIL = "parthittesting@gmail.com"
PASSWORD = "pleasedontchangepassword"

MY_LAT = 18.551451
MY_LONG = 73.934784


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_longitude = float(response.json()["iss_position"]["longitude"])
    iss_latitude = float(response.json()["iss_position"]["latitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_dark():
    paramters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=paramters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.utcnow().hour


    # The response from the sunrise-sunset is in UTC time. It tells me the sunrise and sunset of
    # at position in UTC time, So comparing it with UTC time makes things easier to compare.
    # Or else, I would have to convert the response to IST.


    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    if is_iss_overhead() and is_dark():
        time.sleep(60)
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg="Subject:Look Up\n\nThe ISS is Above you in the Sky")
