# Get api id from https://openweathermap.org/api
# Mail credentials from https://mailtrap.io/

import smtplib
import datetime
import smtplib
import requests

temperatureArr = []
weatherArr = []

# Initial api call
api_address = 'http://api.openweathermap.org/data/2.5/forecast?appid=YourApiId&units=metric&q='
city = input('Input city name: ')

url = api_address + city
json_data = requests.get(api_address).json()

# Initial date time get
date_array = []
today = datetime.date.today()

# Setting dates to array
for i in range(6):
    date = today + datetime.timedelta(days=i)
    formatted_date = date.strftime('%d.%m.%Y')
    date_array.append(formatted_date)

# Fetching wanted information from api
for i in range(39):
    somestring = json_data['list'][i]['dt_txt']
    if "12:00:00" in somestring:
        temperatureArr.append(json_data['list'][i]['main']['temp'])
        weatherArr.append(json_data['list'][i]['weather'][0]['description'])

# Information to be send via email
for i in range(5):
    day = 'Date: ' + date_array[i] + ' 12:00, ' + 'Temperature: ' + str(temperatureArr[i]) + \
       ", " + weatherArr[i]
    msg = msg + day + "\n"

# Email Information
sender = "Mikko Mallikas"
receiver = "Teemu Hirvonen"

message = f"""\
Subject: Weather Forecast
To: {receiver}
From: {sender}

{msg}"""

# Sending email
with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
    server.login("LoginUser", "LoginPass")
    server.sendmail(sender, receiver, message)
