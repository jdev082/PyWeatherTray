import requests, base64, os

api_key = os.environ['OW_API_KEY']
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = os.environ['OW_CITY_NAME']

if "OW_UNIT" in os.environ:
    unit = os.environ['OW_UNIT']
else:
    unit = "imperial"

complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=" + unit

response = requests.get(complete_url)
x = response.json()

def get_weather_temp():
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        z = x["weather"]
        weather_description = z[0]["description"]
        return current_temperature

def get_weather_desc():
        if x["cod"] != "404":
            y = x["main"]
            z = x["weather"]
            icon = z[0]["icon"]
            weather_description = z[0]["description"]
            return weather_description

def get_weather_icon():
    if x["cod"] != "404":
        y = x["main"]
        z = x["weather"]
        icon = z[0]["icon"]
        return icon

def get_icon_data(id):
    icon_id = x['weather'][0]['icon']
    url = 'http://openweathermap.org/img/wn/{icon}.png'.format(icon=icon_id)
    response = requests.get(url, stream=True)
    return base64.encodebytes(response.raw.read())