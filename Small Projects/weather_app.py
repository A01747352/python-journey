""" Necessary Modules:
- requests: To make HTTP requests to the weather API.
- tkinter: To create the GUI for the weather app."""

import requests
import tkinter as tk
from tkinter import messagebox

""" Creating the GUI for the Weather App"""

# Create the main window
root = tk.Tk()
root.title("Weather App")

# Create and configure labels and entry fields
city_label = tk.Label(root, text="Enter City:")
city_label.pack()
city_entry = tk.Entry(root)
city_entry.pack()

# Create a button to fetch weather data
fetch_button = tk.Button(root, text="Fetch Weather")
fetch_button.pack()

# Create a label to display the weather information
weather_label = tk.Label(root, text="")
weather_label.pack()

# Define the function to fetch weather data
def fetch_weather():
    city = city_entry.get()
    api_key = "" # Your OpenWeatherMap API key here

    # Get latitude and longitude of the city
    geo_url = f"https://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={api_key}"
    response = requests.get(geo_url)
    location_data = response.json()

    if location_data:
        lat = location_data[0]["lat"]
        lon = location_data[0]["lon"]

        # Get weather data using latitude and longitude
        weather_url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={api_key}&units=metric"
        response = requests.get(weather_url)
        data = response.json()

        temperature = data["current"]["temp"]
        weather = data["current"]["weather"][0]["description"]
        
        weather_label.config(text=f"Temperature: {temperature}°C\nWeather: {weather}")
    else:
        messagebox.showerror("Error", "City not found")

fetch_button.config(command=fetch_weather)

# Start the GUI main loop
root.mainloop()