import requests
from config import API_KEY  

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raise error for HTTP errors
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
