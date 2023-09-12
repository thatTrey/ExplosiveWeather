import json
import requests
import PySimpleGUI as sg

#url = "https://api.tomorrow.io/v4/weather/realtime?location=indianapolis&apikey="

location = "indianapolis"
apikey = "9xi9ZXm6xNUKDVQDS6DQKsiwtuJMJb61"
units= "imperial"

url = f'https://api.tomorrow.io/v4/weather/realtime?location={location}&units={units}&apikey={apikey}'

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)

"""
data:{
    time:
    values:{
        cloudBase:
        cloudCeiling:
        cloudCover:
        dewPoint:
        freezingRainIntensity:
        humidity:
        precipitationProbability:
        pressureSurfaceLevl:
        rainIntensity:
        sleetIntensity:
        snowIntensity:
        temperature:
        temeratureApparent:
        uvHealthConcern:
        uvIndex:
        visibility:
        weatherCode:
        windDirection:
        windGust:
        windSpeed:
    }
    location:{
        lat:
        lon:
        name:1,2,3,4
        type:
    }
}

"""


# sg.theme('DarkAmber')

# layout = [
#     [sg.Text('GUI Test')],
#     [sg.Text('Please enter a test value'), sg.InputText()],
#     [sg.Button('Ok'), sg.Button('Cancel')]
#     ]

# window = sg.Window('TestWindow', layout)

# while True:
#     event, values = window.read()
#     if event == sg.WIN_CLOSED or event == 'Cancel':
#         break
#     print('You entered ', values[0])

# window.close