
from weather import Weather
#variables assign
weather = Weather
cityname=input("enter city") #input data from user in text form
location = weather.lookup_by_location(cityname)
condition = location.condition()


forecast = location.forecast()
htemp=[] #empty list for high temprature
ltemp=[] #empty list for low temprature

#output data for inputed day
print("current weather is ", condition['text'])
print("current temperature ",condition['temp'])
#data for next days 

print("data for next 5 days are :")

for forecasts in location.forecast():
        htemp = forecasts['high']  #fetching high temp
        ltemp = forecasts['low'] #fetching low temp
        rain= forecast['text'] #data  for rain 
        if forecasts['text']== "Rain":
                print("rain will be on ",forecasts['day'])

#end of prog  task2 --bikramjit singh 
