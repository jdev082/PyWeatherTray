#!/usr/bin/env python3
import pystray
from PIL import Image
from API import *
image = get_icon_data(get_weather_icon)

def after_click(icon, query):
    if str(query) == "Get Weather":
        icon.notify(get_weather_desc())
    elif str(query) == "Exit":
        icon.stop()

icon = pystray.Icon("GFG", image, city_name + "\n" + str(get_weather_temp()) + " Degrees", menu=pystray.Menu(
    pystray.MenuItem("Get Weather", after_click),
    pystray.MenuItem("Exit", after_click)))
 
icon.run()