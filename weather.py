# importing requests and json
import requests, json
# base URL
#BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
BASE_URL = "http://api.openweathermap.org/data/2.5/forecast?"
 #City Name CITY = "Porto"
 #API key API_KEY = "d924d035da69ff52f3677787eee9457b"
openWeatherMapApiKey = "1ae76ac0b8679d9b65ae01f37ea44b16"
id = "1683340"
# upadting the URL
#URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
URL = BASE_URL + "id=" + id + "&appid=" + openWeatherMapApiKey
#URL = "api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=1ae76ac0b8679d9b65ae01f37ea44b16"
# HTTP request
response = requests.get(URL)
# checking the status code of the request
mylist =[]
mylist.append(
	'Temperature\t'
	+'Humidity\t'
	+'Weather\t'
	+'Weather Description\t'
	+'Wind Speed\t'
	+'Wind Degree\t'
	+'Date')
if response.status_code == 200:
	data = response.json()
	for det in data['list']:
		print('tem:',det['main']['temp'],";"
		+'humidity:',det['main']['humidity'],";"
		+'weatherMain:',det['weather'][0]['main'],";"
		+'weatherDescription:',det['weather'][0]['description'],";"
		+'windSpeed:',det['wind']['speed'],";"
		+'windDegree:',det['wind']['deg'],";"
		+'date:',det['dt_txt'])
		mylist.append('{}\t'.format(det['main']['temp'])
		+'{}\t'.format(det['main']['humidity'])
		+'{}\t'.format(det['weather'][0]['main'])
		+'{}\t'.format(det['weather'][0]['description'])
		+'{}\t'.format(det['wind']['speed'])
		+'{}\t'.format(det['wind']['deg'])
		+'{}'.format(det['dt_txt']))
		
else:
   # showing the error message
   print("Error in the HTTP request")
   
with open('forecastedWeather.txt', 'w') as f:
	for line in mylist:
		f.write(line)
		f.write('\n')