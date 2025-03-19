def fetch_weather():
    """Fetch weather data and update the UI"""
    city = city_entry.get().strip()  # Remove extra spaces
    
    if not city:
        messagebox.showerror("Error", "Please enter a city name")
        return
    
    try:
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
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch data: {str(e)}")
