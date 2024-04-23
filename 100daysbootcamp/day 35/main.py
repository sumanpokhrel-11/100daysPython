import requests, os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("API_KEY")
# print(api_key)
api_url = 'https://api.openweathermap.org/data/2.5/onecall'
attributes = {
    'lat': '27.713300',
    'lon' : '85.282398',
    'appid' :api_key,
    'exclude': "current,minutely,daily",
}
will_rain = False
response = requests.get(api_url, params=attributes)
response.raise_for_status()
data = response.json()
weather_slice = data['hourly'][:12]
for hour_data in weather_slice:
    hr_condition = hour_data['weather'][0]['id']
    if int(hr_condition)<700:
        will_rain= True

if will_rain:
    print("Bring and umbrella")