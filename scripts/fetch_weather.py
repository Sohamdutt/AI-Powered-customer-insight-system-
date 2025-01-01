import requests
import json

def fetch_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    weather_data = response.json()

    # Save to a JSON file
    with open(f'./data/raw/weather_{city}.json', 'w') as f:
        json.dump(weather_data, f, indent=4)

    print(f"Weather data for {city} saved.")

# Replace with your API credentials
if __name__ == "__main__":
    fetch_weather(
        api_key="YOUR_API_KEY",
        city="Mumbai"
    )
