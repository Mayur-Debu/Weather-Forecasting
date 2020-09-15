from bs4 import BeautifulSoup
import pandas as pd
import requests
import time

start=time.time()
page=requests.get('https://forecast.weather.gov/MapClick.php?lat=34.05361000000005&lon=-118.24549999999999#.X2D1_2hKi00')

'''Inorder to present the web scrapped data we use this BeautifulSoup module..., 
this module understands the html and css .... and parse them in a lot better way'''

# print(soup)   #Entire page source
soup=BeautifulSoup(page.content,'html.parser')

# print(week)    #source code of a given ID
week=soup.find(id='seven-day-forecast-body')

# print(day_wise_weather_forecast[0]) #source to get day wise weather forecast as the id='seven-day-weather-forecast'
day_wise_weather_forecast=week.find_all(class_='tombstone-container')

#prints weather forecast for a single day
# print(day_wise_weather_forecast[0].find(class_='period-name').get_text())
# print(day_wise_weather_forecast[0].find(class_='short-desc').get_text())
# print(day_wise_weather_forecast[0].find(class_='temp').get_text())

#prints the weather forecast for the week
day=[day.find(class_='period-name').get_text() for day in day_wise_weather_forecast]
weather_on_that_day=[day.find(class_='short-desc').get_text() for day in day_wise_weather_forecast]
temperature_of_that_day=[day.find(class_='temp').get_text() for day in day_wise_weather_forecast]

final_weather_forecast_file=pd.DataFrame\
({
    "DAY:": day,
    "FORECAST:":weather_on_that_day,
    "TEMPERATURE:":temperature_of_that_day
})

final_weather_forecast_file.to_csv('Weather-Forecast.csv')
end=time.time()
print(f'\n[Time taken to scrape web==>{end-start} secs.]')

