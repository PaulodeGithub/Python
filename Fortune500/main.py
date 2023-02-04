import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API =  "Y778W776EHXC17U7"

parameters = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : "TSLA",
    "apikey" : STOCK_API,
}

request = requests.get(STOCK_ENDPOINT, params=parameters)
request.raise_for_status()
data = request.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yes_closing_price = yesterday_data["4. close"]
day_b4_yes= data_list[1]
day_b4_yes_cp = day_b4_yes["4. close"]


print(yes_closing_price, day_b4_yes_cp)


difference= abs(float(yes_closing_price) - float(day_b4_yes_cp))
print(difference)


percentage_difference = ((difference / float(yes_closing_price)) * 100)
print(percentage_difference)
if percentage_difference > 5:
    print("Get news")
else:
    print("Tudo e tranquilo e vc vai dominar Python")


    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
