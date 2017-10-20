
from weather import Weather
#variables assign
weather = Weather()

cityname=input("enter city") #input data from user in text form
location = weather.lookup_by_location(cityname)
condition = location.condition()
print(condition['text'])


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

#Gives you all the days inside a list and the days will be of sublists
all_days=[]

i=0
for forecasts in location.forecast():
    if i<5:
        daily = []
        daily.append(forecasts['text'])
        daily.append(forecasts['date'])
        daily.append(forecasts['high'])
        daily.append(forecasts['low'])
        all_days.append(daily)
        i+=1

print(all_days)


#end of prog  task2 --bikramjit singh 






