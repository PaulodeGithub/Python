import requests
import os
from twilio.rest import Client


account_sid = os.environ.get("ACC_VAR")
auth_token = os.environ.get("AUTH_TOKE")
OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
api_key = os.environ.get("WEATHER_API")


weather_params = {
    "lat": 54.95,
    "lon" : -7.73333, 
    "appid" :api_key,
    "exclude" : "comment,minutely,daily"
    }

response = requests.get(OWM_Endpoint, weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = True

for hour_data in weather_slice:
    condition_code =(hour_data["weather"][0]["id"])
    if int(condition_code) < 700:
        will_rain = True

if will_rain: 
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_='+15417222051',
    body='You are a machine, better keep going',
    to='+353873407070'
    )

    print(message.sid)


# print(weather_data["hourly"][0]["weather"][0]["id"])