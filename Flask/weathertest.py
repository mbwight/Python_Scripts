__author__ = 'Mark'
import pyowm
from flask import Flask
from flask import request
owm = pyowm.OWM('469b2ec82985f979ec625b93836c36bf')

city = "london"
obs = owm.weather_at_place(city)
w = obs.get_weather()
obs_list = owm.weather_at_places(city,searchtype='accurate',limit=3)
temp = w.get_temperature('fahrenheit')
temp = str(temp)
humidity = w.get_humidity()
humidity = str(humidity)
fc = owm.daily_forecast(city, limit=5)
f = fc.get_forecast()
print(obs_list)