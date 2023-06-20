import requests


OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
my_key = "<PUT YOUR KEY HERE!>"


weather_params = {
    "lat": -12.998823,
    "lon" : -38.447058, 
    "appid" : my_key,
    "exclude" : "comment,minutely,daily"
    }

response = requests.get(OWM_Endpoint, weather_params)
response.raise_for_status()
weather_data = response.json()
print(response.status_code)
print(weather_data)