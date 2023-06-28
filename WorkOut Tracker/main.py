
import requests
from datetime import datetime
import os



GENDER= "MALE"
WEIGHT_KG = 86.5
HEIGHT = 176
AGE = 39

APP_ID = os.environ["ENV_APP_ID"]
API_KEY = os.environ["ENV_API_KEY"]

input_question= input("What type of workout did you do?: ")

Exercise_Endpoint= "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_params = {
 "query": input_question,
 "gender":GENDER,
 "weight_kg": WEIGHT_KG,
 "height_cm": HEIGHT,
 "age": AGE
}

headers = {
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY,
    "Content-Type": "application/json",
    
}


date = datetime.now()
today = date.strftime("%d/%m/%Y")
time = date.strftime("        %X")


response = requests.post(url=Exercise_Endpoint, json=exercise_params, headers=headers)
response.raise_for_status()
result = response.json()
print(result)


sheety_post_endpoint = os.environ["SHEET_ENDPOINT"]

bearer_token = {
    "Authorization": f"Bearer {os.enviropn['TOKEN']}"
}


for exercise in result["exercises"]:
    sheety_input = {
            "workout": {
                "date" : today,
                "time" : time,
                "exercise": exercise["name"].title(),
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"]
            
                        }
    }

post = requests.post(url=sheety_post_endpoint, json=sheety_input, headers=bearer_token)
post.raise_for_status()
sheety_result = post.json()
print(result)