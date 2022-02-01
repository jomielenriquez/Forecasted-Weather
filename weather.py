# importing requests and json
import requests, json
import datetime as dt
# base URL
#BASE_URL = "https://api.openweathermap.org/data/2.5/onecall?"
BASE_URL = "http://api.openweathermap.org/data/2.5/forecast?"
 #City Name CITY = "Porto"
 #API key API_KEY = "d924d035da69ff52f3677787eee9457b"
openWeatherMapApiKey = "1ae76ac0b8679d9b65ae01f37ea44b16"
id = "1683340"
# upadting the URL
#URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
#URL = BASE_URL + "id=" + id + "&appid=" + openWeatherMapApiKey
URL = "http://api.openweathermap.org/data/2.5/onecall?lat=14.074368&lon=121.147179&exclude=minutely&appid=1ae76ac0b8679d9b65ae01f37ea44b16"
#URL = "api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=1ae76ac0b8679d9b65ae01f37ea44b16"
# HTTP request
response = requests.get(URL)
# checking the status code of the request
mylist =[]
mylist.append(
	'Temperature\t'
	+'Weather\t'
	+'Date')
if response.status_code == 200:
	data = response.json()
	for det in data['hourly']:
		print('Temp:',det['temp'],';',
                'Weather:',det['weather'][0]['description'],';',
                'Date:',dt.datetime.fromtimestamp(det['dt']).strftime('%Y/%m/%d %H:%M:%S')
                )
                
		mylist.append('{}\t'.format(det['temp'])
		+'{}\t'.format(det['weather'][0]['description'])
		+'{}'.format(dt.datetime.fromtimestamp(det['dt']).strftime('%Y/%m/%d %H:%M:%S')))
		
		
else:
   # showing the error message
   print("Error in the HTTP request")
   
with open('forecastedWeather.txt', 'w') as f:
	for line in mylist:
		f.write(line)
		f.write('\n')
