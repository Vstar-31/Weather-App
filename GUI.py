import tkinter as tk
from tkinter import messagebox
import requests

# API Details
API_KEY = "c20bcc5bca911f60d116478ec23d8e0f"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def fetch_weather():
    """Fetch weather data and update the UI"""
    city = city_entry.get()
    
    if not city:
        messagebox.showerror("Error", "Please enter a city name")
        return
    
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        weather_info = f"City: {data['name']}\n"
        weather_info += f"Temperature: {data['main']['temp']}°C\n"
        weather_info += f"Description: {data['weather'][0]['description']}\n"
        weather_info += f"Humidity: {data['main']['humidity']}%\n"
        weather_info += f"Wind Speed: {data['wind']['speed']} m/s"

        weather_label.config(text=weather_info)
    else:
        messagebox.showerror("Error", "City not found!")

# GUI Setup
root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")

# Input
city_entry = tk.Entry(root, font=("Arial", 14))
city_entry.pack(pady=10)

# Fetch
fetch_button = tk.Button(root, text="Get Weather", command=fetch_weather)
fetch_button.pack()

# Output
weather_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
weather_label.pack(pady=10)


root.mainloop()

