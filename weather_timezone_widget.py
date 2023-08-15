# Weather widget to display weather details of five places given as input

# Import required python packages
from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime, timedelta
import requests
import pytz
from PIL import Image, ImageTk
import os
from dotenv import load_dotenv # pip install python-dotenv. This takes environment variables from .env
import time
from tzwhere import tzwhere
import timezonefinder

#tzwhere = tzwhere.tzwhere()

# Load API key from the environment variables file
load_dotenv()
API_KEY = os.getenv("API_KEY")

root = Tk()
root.title("Weather and Timezone App")
root.geometry("1100x400")
root.config(bg="#00000f")
root.resizable(False, True)

app_name = "Weather widget"

def getWeather(city, cityno):

    geolocator = Nominatim(user_agent=app_name)
    location = geolocator.geocode(city)
    
    tf = timezonefinder.TimezoneFinder()

    # From the lat/long, get the tz-database-style time zone name (e.g. 'Europe/Paris') or None
    timezone_str = tf.certain_timezone_at(lng=location.longitude,lat=location.latitude)

    timezone = pytz.timezone(timezone_str)
    local_time = datetime.now(timezone)
    current_time = local_time.strftime("%B %d, %Y %I:%M %p")

    # weather info from open weather map api
    api = "https://api.openweathermap.org/data/2.5/weather?lat="\
        +str(location.latitude)\
        +"&lon="+str(location.longitude)\
        +"&units=metric"\
        +"&appid="+str(API_KEY)
    
    json_data = requests.get(api).json()

    # Current temperature
    temp = json_data['main']['temp']
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed'] 
    description = json_data['weather'][0]['description']

    if cityno == 1:
        place1.config(text=(f'{city}'))
        t11.config(text=(f'{temp} °C'))
        h12.config(text=(f'{humidity} %'))
        p13.config(text=(f'{pressure} hPa'))
        w14.config(text=(f'{wind} m/s'))
        d15.config(text=(f'{description}'))
        tz15.config(text=(f'{current_time}'))
        timezone16.config(text=(f'{timezone}'))
    elif cityno == 2:
        place2.config(text=(f'{city}'))
        t21.config(text=(f'{temp} °C'))
        h22.config(text=(f'{humidity} %'))
        p23.config(text=(f'{pressure} hPa'))
        w24.config(text=(f'{wind} m/s'))
        d25.config(text=(f'{description}'))
        tz25.config(text=(f'{current_time}'))
        timezone26.config(text=(f'{timezone}'))
    elif cityno == 3:
        place3.config(text=(f'{city}'))
        t31.config(text=(f'{temp} °C'))
        h32.config(text=(f'{humidity} %'))
        p33.config(text=(f'{pressure} hPa'))
        w34.config(text=(f'{wind} m/s'))
        d35.config(text=(f'{description}'))
        tz35.config(text=(f'{current_time}'))
        timezone36.config(text=(f'{timezone}'))
    elif cityno == 4:
        place4.config(text=(f'{city}'))
        t41.config(text=(f'{temp} °C'))
        h42.config(text=(f'{humidity} %'))
        p43.config(text=(f'{pressure} hPa'))
        w44.config(text=(f'{wind} m/s'))
        d45.config(text=(f'{description}'))
        tz45.config(text=(f'{current_time}'))
        timezone46.config(text=(f'{timezone}'))
    elif cityno == 5:
        place5.config(text=(f'{city}'))
        t51.config(text=(f'{temp} °C'))
        h52.config(text=(f'{humidity} %'))
        p53.config(text=(f'{pressure} hPa'))
        w54.config(text=(f'{wind} m/s'))
        d55.config(text=(f'{description}'))
        tz55.config(text=(f'{current_time}'))
        timezone56.config(text=(f'{timezone}'))

    print(f'Place name: {city} temperature {temp} pressure {pressure}\
          humidity {humidity} wind speed {wind} Description {description}')

# import weather icon
image_icon = PhotoImage(file="Images/weather_icon1.png")
root.iconphoto(False, image_icon)

rect_box = PhotoImage(file="Images/rectangularbox.png")
rbox = 1
while rbox < 6:
    box_name = 'Round_box'+str(rbox)
    xpos = [30, 230, 430, 630, 830]
    box_name = rect_box
    Label(root, image=box_name,bg="#00000f").place(x=xpos[rbox-1],y=60)
    rbox += 1

i = 1
j = 1
xval1 = 40
# Loop through to position the labels in each of the rectangular boxes
while j < 6:
    while i < 6:
        label_name = 'label'+str(j)+str(i)
        
        label_list = ['Temperature', 'Humidity', 'Pressure', 'Wind speed', 'Description']
        yval = [150, 180, 210, 240, 270, 300]
        label_name = Label(root, text=label_list[i-1],font=("Calibri", 10, 'bold'), fg="white", bg='grey')
        label_name.place(x=xval1, y=yval[i-1])
        
        i += 1    
        if i == 6:
            j += 1
            i = 1
            xval1 += 200
            break


# place name values placeholders
place1 = Label(root,font=("Arial", 16, 'bold'), fg="black", bg='yellow')
place1.place(x=80, y=70)

place2 = Label(root,font=("Arial", 16, 'bold'), fg="black", bg='yellow')
place2.place(x=280, y=70)

place3 = Label(root,font=("Arial", 16, 'bold'), fg="black", bg='yellow')
place3.place(x=480, y=70)

place4 = Label(root,font=("Arial", 16, 'bold'), fg="black", bg='yellow')
place4.place(x=680, y=70)

place5 = Label(root,font=("Arial", 16, 'bold'), fg="black", bg='yellow')
place5.place(x=880, y=70)

# Temperature, pressure, humidity, wind speed and description values placeholders - Set 1
t11 = Label(root,font=("Calibri", 11, 'bold'), fg="black", bg='yellow')
t11.place(x=120, y=150)

h12 = Label(root,font=("Calibri", 11, 'bold'), fg="black", bg='yellow')
h12.place(x=120, y=180)

p13 = Label(root,font=("Calibri", 11, 'bold'), fg="black", bg='yellow')
p13.place(x=120, y=210)

w14 = Label(root,font=("Calibri", 11, 'bold'), fg="black", bg='yellow')
w14.place(x=120, y=240)

d15 = Label(root,font=("Calibri", 11, 'bold'), fg="black", bg='yellow')
d15.place(x=120, y=270)

tz15 = Label(root,font=("Calibri", 9, 'bold'), fg="black", bg='yellow')
tz15.place(x=50, y=100)

timezone16 = Label(root,font=("Calibri", 9, 'bold'), fg="black", bg='yellow')
timezone16.place(x=80, y=120) 

# Temperature, pressure, humidity, wind speed and description values placeholders - Set 2
t21 = Label(root,font=("Calibri", 11, 'bold'), fg="black", bg='yellow')
t21.place(x=320, y=150)

h22 = Label(root,font=("Calibri", 11, 'bold'), fg="black", bg='yellow')
h22.place(x=320, y=180)

p23 = Label(root,font=("Calibri", 11, 'bold'), fg="black", bg='yellow')
p23.place(x=320, y=210)

w24 = Label(root,font=("Calibri", 11, 'bold'), fg="black", bg='yellow')
w24.place(x=320, y=240)

d25 = Label(root,font=("Calibri", 11, 'bold'), fg="black", bg='yellow')
d25.place(x=320, y=270)

tz25 = Label(root,font=("Calibri", 9, 'bold'), fg="black", bg='yellow')
tz25.place(x=250, y=100)

timezone26 = Label(root,font=("Calibri", 9, 'bold'), fg="black", bg='yellow')
timezone26.place(x=280, y=120) 

# Temperature, pressure, humidity, wind speed and description values placeholders - Set 3
t31 = Label(root,font=("Calibri", 11, 'bold'), fg="black", bg='yellow')
t31.place(x=520, y=150)

h32 = Label(root,font=("Calibri", 11, 'bold'), fg="black", bg='yellow')
h32.place(x=520, y=180)

p33 = Label(root,font=("Calibri", 11, 'bold'), fg="black", bg='yellow')
p33.place(x=520, y=210)

w34 = Label(root,font=("Calibri", 11, 'bold'), fg="black", bg='yellow')
w34.place(x=520, y=240)

d35 = Label(root,font=("Calibri", 11, 'bold'), fg="black", bg='yellow')
d35.place(x=520, y=270)

tz35 = Label(root,font=("Calibri", 9, 'bold'), fg="black", bg='yellow')
tz35.place(x=450, y=100)

timezone36 = Label(root,font=("Calibri", 9, 'bold'), fg="black", bg='yellow')
timezone36.place(x=480, y=120) 

# Temperature, pressure, humidity, wind speed and description values placeholders - Set 4
t41 = Label(root,font=("Calibri", 11, 'bold'), fg="black", bg='yellow')
t41.place(x=720, y=150)

h42 = Label(root,font=("Calibri", 11, 'bold'), fg="black", bg='yellow')
h42.place(x=720, y=180)

p43 = Label(root,font=("Calibri", 11, 'bold'), fg="black", bg='yellow')
p43.place(x=720, y=210)

w44 = Label(root,font=("Calibri", 11, 'bold'), fg="black", bg='yellow')
w44.place(x=720, y=240)

d45 = Label(root,font=("Calibri", 11, 'bold'), fg="black", bg='yellow')
d45.place(x=720, y=270)

tz45 = Label(root,font=("Calibri", 9, 'bold'), fg="black", bg='yellow')
tz45.place(x=650, y=100)

timezone46 = Label(root,font=("Calibri", 9, 'bold'), fg="black", bg='yellow')
timezone46.place(x=680, y=120) 

# Temperature, pressure, humidity, wind speed and description values placeholders - Set 5
t51 = Label(root,font=("Calibri", 11, 'bold'), fg="black", bg='yellow')
t51.place(x=920, y=150)

h52 = Label(root,font=("Calibri", 11, 'bold'), fg="black", bg='yellow')
h52.place(x=920, y=180)

p53 = Label(root,font=("Calibri", 11, 'bold'), fg="black", bg='yellow')
p53.place(x=920, y=210)

w54 = Label(root,font=("Calibri", 11, 'bold'), fg="black", bg='yellow')
w54.place(x=920, y=240)

d55 = Label(root,font=("Calibri", 11, 'bold'), fg="black", bg='yellow')
d55.place(x=920, y=270)

tz55 = Label(root,font=("Calibri", 9, 'bold'), fg="black", bg='yellow')
tz55.place(x=850, y=100)

timezone56 = Label(root,font=("Calibri", 9, 'bold'), fg="black", bg='yellow')
timezone56.place(x=880, y=120) 

# creating an empty place list
city_list = []
 
# number of elements if the place as integer input
n = int(input("Enter number of place names : "))
 
if n> 0 and n <= 5:
    # iterating till the range to load the place name to the list from the user input
    for idx in range(0, n):
        city_name = input(f'Enter place name {idx+1} : ')
        # adding the element
        city_list.append(city_name)
# Exit the program with message
else:
    print('The limit for the number of places input is 5, enter a number equal to or below 5')
    exit()
    

print(f'Loading weather data from cities in list \n {city_list}')

cityno = 1
for city in city_list:
    getWeather(city, cityno)
    cityno += 1
    time.sleep(3)

root.mainloop()