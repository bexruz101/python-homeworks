import requests


def fetch_weather(city):
    api_key = "e3f14178c2a157a60f27512944cdd188"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",  # Use 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if data["cod"] == 200:
            # Extract relevant information
            weather_info = {
                "City": data["name"],
                "Temperature": data["main"]["temp"],
                "Humidity": data["main"]["humidity"],
                "Description": data["weather"][0]["description"],
            }

            # Print the weather information
            print(f"Weather in {weather_info['City']}:")
            print(f"Temperature: {weather_info['Temperature']}°C")
            print(f"Humidity: {weather_info['Humidity']}%")
            print(f"Description: {weather_info['Description']}")

        else:
            print(f"Error: {data['message']}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")


# Example usage:
fetch_weather("Tashkent")  # Replace 'Tashkent' with any city you want to fetch data for
