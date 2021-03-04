import requests
from datetime import datetime

USERNAME = "bigdaddystinkyfeet"
TOKEN = "blahblahblacksheep12345"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",

}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id" : "graph1",
    "name" : "Running Graph",
    "unit" : "Km",
    "type" : "float",
    "color" : "sora",
}

headers = {
    "X-USER-TOKEN" : TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

post_pixel_endpoint = f"{graph_endpoint}/graph1"

today = datetime.now()

pixel_config = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : "10.0",
}

# response = requests.post(post_pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)


formatted_today = today.strftime("%Y%m%d")
update_pixel_endpoint = f"{graph_endpoint}/graph1/{formatted_today}"
update_config = {
    "quantity" : "10.0",
}

# response = requests.put(url=update_pixel_endpoint, json=update_config, headers=headers)
# print(response)


delete_day_pixel_endpoint = f"{graph_endpoint}/graph1/{formatted_today}"
response = requests.delete(url=delete_day_pixel_endpoint, headers=headers)
print(response)

