import os
import requests
import json
import time


def get_ip_address():
    # Fetch the public IP address using curl ifconfig.me
    ip_address = os.popen("curl -s ifconfig.me").read().strip()
    return ip_address


def get_cached_ip():
    try:
        with open("ip_cache.json", "r") as file:
            data = json.load(file)
            last_updated = data.get("last_updated")
            # print(last_updated)
            # exit()
            if last_updated and time.time() - last_updated < 24 * 3600:
                return data.get("city")
    except FileNotFoundError:
        pass
    return None


def update_ip_cache(city):
    data = {"city": city, "last_updated": time.time()}
    with open("ip_cache.json", "w") as file:
        json.dump(data, file)


def get_city_name(ip, access_key):
    cached_ip = get_cached_ip()
    if cached_ip:
        return cached_ip.replace(" ", "%20")

    url = f"https://apiip.net/api/check?ip={ip}&accessKey={access_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # print(data)
        city = data.get("city")
        # print(city)
        update_ip_cache(city)
        return city.replace(" ", "%20")  # Replace spaces with %20 in URL
    else:
        print("Failed to retrieve city name.")
        return None


def get_cached_weather(city_name):
    try:
        with open("weather_cache.json", "r") as file:
            data = json.load(file)
            last_updated = data.get("last_updated")
            if last_updated and time.time() - last_updated < 30 * 60:
                return data.get(city_name)
    except FileNotFoundError:
        pass
    return None


def update_weather_cache(city_name, weather_data):
    try:
        with open("weather_cache.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    data[city_name] = {"data": weather_data, "last_updated": time.time()}

    with open("weather_cache.json", "w") as file:
        json.dump(data, file)


def get_weather(city_name, api_key):
    cached_weather = get_cached_weather(city_name)
    if cached_weather:
        return cached_weather["data"]

    if city_name:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
        # print(url)
        response = requests.get(url)
        # print(response)
        if response.status_code == 200:
            weather_data = response.json()
            update_weather_cache(city_name, weather_data)
            return weather_data
        else:
            print("Failed to retrieve weather information.")
    else:
        print("City name not provided.")


weather_data = None
try:
    # Get the IP address
    ip_address = get_ip_address()
    # print("IP Address:", ip_address)

    # Get the city name
    city_name = get_city_name(ip_address, "")
    print(city_name.replace("%20", " "))

    # Fetch weather for the city
    weather_data = get_weather(city_name, "")
    if weather_data:
        temperature = weather_data["main"]["temp"]
        weather_description = weather_data["weather"][0]["description"]
        # print(f"Weather in {city_name.replace}:")
        print(f"{temperature}°C | {weather_description}")
except:
    print("failed to fetch weather data")
