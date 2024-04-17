import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status() #this will generate an http error if there is error
print(response.status_code)
data = response.json()
message = data['message']
longitude = data['iss_position']['longitude']

print(data)
print(message)
print(longitude)