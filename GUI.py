import tkinter as tk
from tkinter import messagebox
from weather_api import get_weather

def fetch_weather():
    city = city_entry.get()
    weather_data = get_weather(city)

    if "error" in weather_data:
        messagebox.showerror("Error", weather_data["error"])
    else:
        weather_desc = weather_data["weather"][0]["description"]
        temp = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]
        result_label.config(text=f"🌤️ {weather_desc}\n🌡️ {temp}°C\n💧 {humidity}%\n💨 {wind_speed} m/s")

# GUI Setup
root = tk.Tk()
root.title("Weather App")
root.geometry("300x250")

tk.Label(root, text="Enter City:", font=("Arial", 14)).pack(pady=10)
city_entry = tk.Entry(root, font=("Arial", 14))
city_entry.pack()

tk.Button(root, text="Get Weather", font=("Arial", 14), command=fetch_weather).pack(pady=10)
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack()

root.mainloop()
