import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
longitude = response.json()["iss_position"]["longitude"]
latitude = response.json()["iss_position"]["latitude"]

print(longitude, latitude)

