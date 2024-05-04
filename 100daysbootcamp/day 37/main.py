import requests
import datetime
TOKEN = "gahganigah343hgh1"
USERNAME = "sumanpok11"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    # create a random token
    "token" : TOKEN,
    "username": USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}

# step: 1 uncomment these line on 15, 16 and run once to create a username and once created than comment these lines
# reponse = requests.post(url = pixela_endpoint, json = user_params)
# print(reponse.text)

# step 2: creating graphs

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id" : GRAPH_ID,
    "name" : "Walking Graph",
    "unit": "Step",
    "type": "int",
    "color": "ajisai"
}
header = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url = graph_endpoint, json=graph_config, headers= header)
# print(response.text)


# step 3
three_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.datetime.now()
three_params = {
    "date" : today.strftime("%Y%m%d"),
    "quantity": input("Enter how many steps did you walk today by dividing it with 100: "),
}
response = requests.post(url=three_endpoint, json=three_params, headers = header)
print(response.text)


# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# new_pixel_data = {
#     "quantity": "100"
# }

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=header)
# print(response.text)


# delete_endpoint = update_endpoint

# response = requests.delete(url=delete_endpoint, headers=header)
# print(response.text)