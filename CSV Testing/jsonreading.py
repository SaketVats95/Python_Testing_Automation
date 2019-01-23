import json

stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0,"felineIQ": null}'

jsondataAsPythonValue=json.loads(stringOfJsonData)

print(str(jsondataAsPythonValue))

import requests, sys

# Compute location from command line arguments.
if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')


print(sys.argv[1])
location = ' '.join(sys.argv[1:])
print(location)