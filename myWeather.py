# - - - - - - - - - - - - - - - - - 
# Date:    2025-01-05
# Author:  Brian Harkness
# Remarks: Command line weather getter for learning mostly
#          
#
# Links:   https://developers.google.com/maps/documentation/geocoding/overview \
#          https://weather-gov.github.io/api/gridpoints \
#
#
# Changes:
#
# - - - - - - - - - - - - - - - - 

import requests
import os

# api.weather.gov url below is using lat,lng coordinates to get the weather forecast
# This function uses maps.googelapis.com to get the lat,lng coordinates of a location
def get_coordinates(zip_code, api_key):
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "address": zip_code,
        "key": api_key
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if data["status"] == "OK":
        location = data["results"][0]["geometry"]["location"]
        return location["lat"], location["lng"]
    else:
        return None

# This function gets the weather forecast for a location and prints to STDOUT
def get_weather(location):
    api_key = os.environ["GEOCODE_API_KEY"]
    coordinates = get_coordinates(location, api_key)
    if not coordinates:
        print("Invalid location")
        return
    
    lat, lng = coordinates
    base_url = f"https://api.weather.gov/points/{lat},{lng}"

    response = requests.get(base_url)
    data = response.json()

    if "properties" not in data:
        print("Error retrieving weather data")
        return

    location = data["properties"]["relativeLocation"]["properties"]
    city = location["city"]
    state = location["state"]
    print(f"\nWeather forecast for {city}, {state}\n")

    forecast_url = data["properties"]["forecast"]

    response = requests.get(forecast_url)
    forecast_data = response.json()

    if "properties" not in forecast_data or "periods" not in forecast_data["properties"]:
        print("Error retrieving forecast data")
        return

    print("Forecast:")
    for period in forecast_data["properties"]["periods"]:
        print(f"\n---\n{period['name']}: {period['detailedForecast']}\n")

# Entry point of the script
if __name__ == "__main__":
    location = input("Enter a location: ")
    get_weather(location)
