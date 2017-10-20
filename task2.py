#from flask import flask
from weather import Weather
weather = Weather
cityname=input("enter city")
location = weather.lookup_by_location(cityname)
condition = location.condition()


forecast = location.forecast()
htemp=[] #empty list for high temprature
ltemp=[] #empty list for low temprature

#output data for inputed day
print("current weather is ", condition['text'])
print("current temperature ",condition['temp'])

