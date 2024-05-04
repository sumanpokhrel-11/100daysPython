import requests
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

three_params = {
    "date" : "20240504",
    "quantity": "39",
}
response = requests.post(url=three_endpoint, json=three_params, headers = header)
print(response.text)