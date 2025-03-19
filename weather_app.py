import requests

API_KEY = "c20bcc5bca911f60d116478ec23d8e0f"  #API KEY
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    """Fetch weather data from OpenWeatherMap API"""
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Fetch temperature in Celsius
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    
    if response.status_code == 200:
        weather_info = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
        return weather_info
    else:
        return {"error": "City not found!"}

# Test with a city
if __name__ == "__main__":
    city = input("Enter city name: ")
    weather = get_weather(city)
    print(weather)

