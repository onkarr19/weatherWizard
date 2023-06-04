import requests
import json
import sys
import os
from dotenv import load_dotenv
import numpy as np

load_dotenv()


def get_weather(city):
    api_key = os.getenv('OPENWEATHERAPP_API_KEY') 
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # You can change the units to metric, imperial, or standard
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes

        data = response.json()

        # Extract relevant weather information
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        # Print the weather forecast
        print(f"Weather forecast for {city}:")
        print(f"Description: {weather_description}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")

    except requests.exceptions.HTTPError as e:
        print(f"Error: {e}")
    except KeyError:
        print(f"Error: Failed to parse weather data for {city}")
    except json.JSONDecodeError:
        print("Error: Failed to decode weather data")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        city_name = sys.argv[1]
        get_weather(city_name)
    else:
        print("Please provide a city name as an argument.")
