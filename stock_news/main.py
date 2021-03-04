STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY_ALPHAVANTAGE = "E1H815SN5RP0R54D"
NEWS_API = "3042b058f0664d18972d006c42a94fdb"
TWILIO_API = "ACa91b586230ade1ad8f0362bf9ba516df"
TWILIO_AUTH = "8afd7ce23e92e1212d541df9cfdc61aa"
PHONE_NUMBER = "+14159491523"
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

import requests


response = requests.get(url=f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey={API_KEY_ALPHAVANTAGE}")
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data['4. close'])
print(yesterday_closing_price)

day_before_yesterday = data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday['4. close'])
print(day_before_yesterday_closing_price)

difference = (day_before_yesterday_closing_price-yesterday_closing_price)
print(difference)

up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percentage = round(abs((difference / yesterday_closing_price) * 100))
print(diff_percentage)


if diff_percentage >= 5:
    news_response = requests.get(url=f"http://newsapi.org/v2/everything?q=tesla&qInTitle=tesla&from=2021-02-04&sortBy=publishedAt&apiKey={NEWS_API}")
    news_response.raise_for_status()
    three_articles = news_response.json()["articles"][:3]
    print(three_articles)

    articles_list = [f"\n\n{STOCK}:{up_down}{diff_percentage}%\n\nHeadline: {article['title']}\nBrief: {article['description']}" for article in three_articles]



    from twilio.rest import Client


    # Your Account Sid and Auth Token from twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = TWILIO_API
    auth_token = TWILIO_AUTH
    client = Client(account_sid, auth_token)

    for article in articles_list:
        message = client.messages \
                        .create(
                             body=article,
                             from_=PHONE_NUMBER,
                             to='PARTHIT_PHONE_NUMBER'
                         )

        print(message.sid)