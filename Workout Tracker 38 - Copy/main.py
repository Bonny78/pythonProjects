import os

import requests
import datetime

APP_ID = "8d99ec9e"
API_KEY = "87285cc521e4d70e907568418aea31a9"
GENDER = "Female"
WEIGHT_KG = 51.2
HEIGHT_CM = 162.6
AGE = 25
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/801d627059cb6f98e7e3e9308b47a1b3/workoutTracking/workouts"



exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

today_date = datetime.datetime.now().strftime("%d/%m/%Y")
now_time = datetime.datetime.now().strftime("%X")

bearer_headers = {
    "Authorization": f"Bearer {os.environ.get('TOKEN')}"
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheety_endpoint, json=sheet_inputs, headers=bearer_headers)

    print(sheet_response.text)
