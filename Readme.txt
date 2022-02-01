Created by Jomiel Enriquez
November 21, 2021

1. Install python using this link https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe
2. Install requests on python. Follow this link https://pypi.org/project/requests/
3. Register on open weather map
4. Get your API and ID in open weather map
5. Run the code in python
  -steps on running the code
  1. open cmd
  2. change the directory to the location of the file
  3. enter 'python <filename.py>' in cmd

test
--Request using city id as parameter
http://api.openweathermap.org/data/2.5/forecast?id=1683340&appid=1ae76ac0b8679d9b65ae01f37ea44b16


--Request using latitude and longitude as parameter
--Detailed Intruction: https://openweathermap.org/api/one-call-api
https://api.openweathermap.org/data/2.5/onecall?lat=14.074368&lon=121.147179&exclude=hourly&appid=1ae76ac0b8679d9b65ae01f37ea44b16

Hourly
https://api.openweathermap.org/data/2.5/forecast/hourly?lat=14.074368&lon=121.147179&appid=1ae76ac0b8679d9b65ae01f37ea44b16

https://api.openweathermap.org/data/2.5/onecall?lat=14.074368&lon=121.147179&exclude=hourly&appid=1ae76ac0b8679d9b65ae01f37ea44b16

minutely
https://api.openweathermap.org/data/2.5/onecall?lat=14.074368&lon=121.147179&exclude=minutely&appid=1ae76ac0b8679d9b65ae01f37ea44b16
