import requests

def get_weather(city):
    # Example API call to get weather
    response = requests.get(f"http://api.weatherapi.com/v1/current.json?key=your_weather_api_key&q={city}")
    data = response.json()
    if data.get("current"):
        temperature = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        return f"The current temperature in {city} is {temperature}°C with {condition}."
    return f"Sorry, I couldn't fetch the weather for {city}."
