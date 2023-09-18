import requests

API_KEY = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


def fetch_weather(city_name):
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric",  # Use 'imperial' for Fahrenheit
    }

    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        main_data = data["main"]
        temperature = main_data["temp"]
        feels_like = main_data["feels_like"]
        weather_description = data["weather"][0]["description"]

        print(f"Weather in {city_name}:")
        print(f"Temperature: {temperature}°C")
        print(f"Feels Like: {feels_like}°C")
        print(f"Description: {weather_description.capitalize()}")
    else:
        print(
            f"Failed to fetch weather for {city_name}. Please check the city name and your API key."
        )


if __name__ == "__main__":
    city = input("Enter the name of the city: ")
    fetch_weather(city)
