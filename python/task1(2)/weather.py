# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 19:21:10 2023

@author: madhu
"""
import requests

def fetch_weather_data(city_name, api_key):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data

def display_weather_data(data):
    if data['cod'] == 200:
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        print(f"Weather: {weather}")
        print(f"Temperature: {temperature}°C")
    else:
        print("City not found.")

def main():
    city_name = input("Enter city name: ")
    api_key = "09265c6a4c032fa1f98b858276edbbe7" 
    weather_data = fetch_weather_data(city_name, api_key)
    display_weather_data(weather_data)

if __name__ == '__main__':
    main()
