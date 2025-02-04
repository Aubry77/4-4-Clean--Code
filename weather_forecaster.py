# Weather Forecast Application Script

class WeatherDataFetcher:
    def fetch_weather_data(self, city):
        # Simulated function to fetch weather data for a given city
        print(f"\033[1;34mFetching weather data for {city}...\033[0m")
        # Simulated data based on city
        weather_data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
        }
        return weather_data.get(city, None)

class WeatherDataParser:
    def parse_weather_data(self, weather_data):
        if weather_data:
            temperature = weather_data["temperature"]
            condition = weather_data["condition"]
            humidity = weather_data["humidity"]
            city = weather_data["city"]
            return f"\033

        