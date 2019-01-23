import smtplib,requests,json
from _datetime import datetime
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
count=1
weatherMsg=''

for i in w:
    #print(i['dt_txt'],' date-time weather condition in : %s' %(location))

    #print(i['weather'][0]['main'],' - ',i['weather'][0]['description'])
    if i['dt_txt'][8:10]== str(datetime.now())[8:10] and count<10:

        weatherMsg=weatherMsg + i['dt_txt'] +' date-time weather condition in : '+ location +"\n\n"
        weatherMsg= weatherMsg+ i['weather'][0]['main']+' - '+i['weather'][0]['description'] + "\n"
        weatherMsg = weatherMsg + "Minimum Temperature : "+ str(i['main']['temp_min']-273) +"\n"
        weatherMsg = weatherMsg + "Minimum Temperature : " + str(i['main']['temp_max']-273) + "\n"
        count+=1
print(weatherMsg)

toList=["saketvatslpu@gmail.com","ss066137@gmail.com","jeevanjc92@gmail.com","mehta08rohan@gmail.com","rajamanikanta03@gmail.com",]

smtpObj=smtplib.SMTP("smtp.gmail.com",587)
print(smtpObj.ehlo())
print(smtpObj.starttls())
print(smtpObj.login('MarlinX1120@gmail.com', ' PASSWORD'))
print(smtpObj.sendmail(from_addr='MarlinX1120@gmail.com', to_addrs=toList, msg='Subject: Weather Details.\nHell All, \nPlease find the Today\'s Weather Report:\n\n'+weatherMsg+"\n\n Thanks"))
smtpObj.quit()