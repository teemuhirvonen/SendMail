import smtplib
import datetime
import smtplib
import requests

temperatureArr = []
weatherArr = []

# API haku
api_address = 'http://api.openweathermap.org/data/2.5/forecast?appid=APPID&units=metric&q=Helsinki'
#city = input('Input city name: ')

#url = api_address + city
json_data = requests.get(api_address).json()

# Päivä tiedot
date_array = []
today = datetime.date.today()

# Päivämäärän asetus
for i in range(6):
    date = today + datetime.timedelta(days=i)
    formatted_date = date.strftime('%d.%m.%Y')
    date_array.append(formatted_date)

# Tietojen haku APIsta
for i in range(39):
    somestring = json_data['list'][i]['dt_txt']
    if "12:00:00" in somestring:
        temperatureArr.append(json_data['list'][i]['main']['temp'])
        weatherArr.append(json_data['list'][i]['weather'][0]['description'])

# Lähetettävät tiedot
day1 = 'Date: ' + date_array[0] + ' 12:00, ' + 'Temperature: ' + str(temperatureArr[0]) + \
       ", " + weatherArr[0]

day2 = 'Date: ' + date_array[1] + ' 12:00, ' + 'Temperature: ' + str(temperatureArr[1]) + \
       ", " + weatherArr[1]

day3 = 'Date: ' + date_array[2] + ' 12:00, ' + 'Temperature: ' + str(temperatureArr[2]) + \
       ", " + weatherArr[2]

day4 = 'Date: ' + date_array[3] + ' 12:00, ' + 'Temperature: ' + str(temperatureArr[3]) + \
       ", " + weatherArr[3]

day5 = 'Date: ' + date_array[4] + ' 12:00, ' + 'Temperature: ' + str(temperatureArr[4]) + \
       ", " + weatherArr[4]

msg = day1 + '\n' + day2 + '\n' + day3 + '\n' + day4 + '\n' + day5

# Sähköpostin tiedot
sender = "Mikko Mallikas"
receiver = "Teemu Hirvonen"

message = f"""\
Subject: Weather Forecast
To: {receiver}
From: {sender}

{msg}"""

# Sähköpostin lähetys
with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
    server.login("LoginUser", "LoginPass")
    server.sendmail(sender, receiver, message)