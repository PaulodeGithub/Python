import requests


OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
my_key = "INSERT YOUR API KEY HERE!"


weather_params = {
    "lat": 54.95,
    "lon" : -7.73333, 
    "appid" : my_key,
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
    print("Your gona need to bring your umbrella")


# print(weather_data["hourly"][0]["weather"][0]["id"])