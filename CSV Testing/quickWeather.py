#! python3
# quickWeather.py - Prints the current weather for a location from the command line.

import json, requests, sys

# Compute location from command line arguments.
if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
        #sys.exit()
    location = 'Thane,IN'#' '.join(sys.argv[1:])

    # Download the JSON data from OpenWeatherMap.org's API
    url ='http://api.openweathermap.org/data/2.5/forecast?q=%s&APPID=11e0dc9689af7dd460320ba4145d0171' % (location)
    print(url)
    response = requests.get(url)
    response.raise_for_status()

    # Load JSON data into a Python variable.
    weatherData = json.loads(response.text)

    # Print weather descriptions.
    w = weatherData['list']

    for i in w:
        print(i['dt_txt'],' date-time weather condition in : %s' %(location))
        print(i['weather'][0]['main'],' - ',i['weather'][0]['description'])
