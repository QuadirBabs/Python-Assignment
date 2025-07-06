import requests
from dotenv import load_dotenv
import os
from pprint import pprint
load_dotenv()

def get_current_weather():
    print("\n***Get current weather conditions****\n") 
    
    city = input("\n Please input a city name:\n") 

    request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=Metric"

    # print(request_url)
    
    weather_data = requests.get(request_url).json()
    print(f"\n The current weather condition for {weather_data["name"]}\n ")
    print(f"\n The current weather temperature is {weather_data["main"]["temp"]}\n ")
    print(f"\n Feels like the {weather_data["main"]["feels_like"]} and {weather_data["weather"][0]["description"]}\n ")
    
    # pprint(weather_data)
    
if __name__ == "__main__":
    get_current_weather()