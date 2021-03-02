import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient


MY_API_KEY = "6528246b9100bf789a0895bae7a3a0a8"
PHONE_NUMBER = "+14159491523"
# API_KEY =    "69f04e4613056b159c2761a9d9e664d2"
# WORKED = "https://api.openweathermap.org/data/2.5/onecall?lat=18.5204&lon=73.8567&exclude=hourly&appid=6528246b9100bf789a0895bae7a3a0a8"
LAT = 18.5204
LONG = 73.8567
URL = f"https://api.openweathermap.org/data/2.5/onecall?lat={LAT}&lon={LONG}&exclude=current,minutely,daily&appid={MY_API_KEY}"
account_sid = "ACa91b586230ade1ad8f0362bf9ba516df"
auth_token = "66b7f5de249b5d929c96032005541f47"



import requests


response = requests.get(url=URL)
response.raise_for_status()
weather_data = response.json()

first_twelve_hour_data = weather_data['hourly'][:12]

will_rain = False

for hour in first_twelve_hour_data:
    if hour['weather'][0]['id'] < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': "https_proxy"}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="Carry an Umbrella ☔️ . Hope you have a great day. From Parthit in 02-March-2021",
        from_=PHONE_NUMBER,
        to='PARTHIT_PHONE_NUMBER'
    )
    print(message.status)
else:
    print('No need for an umbrella today')