import requests
import os

def get_secret_key():
    secret_key = os.getenv('WEATHER_API_KEY')
    if secret_key is None:
        raise ValueError("WEATHER_API_KEY environment variable not set.")
    return secret_key

if __name__ == "__main__":
    try:
        secret_key = get_secret_key()
        print(f"Retrieved secret key: {secret_key}")
    except ValueError as e:
        print(e)



city = input('What city would you like the weather for?\n')
url = 'http://api.weatherapi.com/v1/current.json?key='+secret_key+'&q='+city+'&aqi=no'
response = requests.get(url)
weather_json = response.json()
temp = weather_json.get('current').get('temp_f')
description = weather_json.get('current').get('condition').get('text')
wind_mph = weather_json.get('current').get('wind_mph')
wind_dir = weather_json.get('current').get('wind_dir')

# print("Today's weather in", city, "is", description, 'and', temp, "degrees F.")
print("Today's weather in", city, "is", description, 'and', temp, "degrees. The winds are blowing", wind_dir, 'at', wind_mph, 'miles per hour.')