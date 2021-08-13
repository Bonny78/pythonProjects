import requests
import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USER_NAME = "bonnie12"
TOKEN = "knkwndkwn1k382bsj"
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}
#this post for GRAPH
# response =requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

post_pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"

today = datetime.datetime.now()
formatted_today_date = today.strftime("%Y%m%d")

post_pixel_params = {
    "date": formatted_today_date,
    "quantity": input("How many Kilometers did you cycle today? "),
}
#this post for entering quantity
response = requests.post(url=post_pixel_endpoint, json=post_pixel_params, headers=headers)
print(response.text)

put_params = {
    "quantity": "12.5"
}
update_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{formatted_today_date}"

# response =requests.put(url=update_endpoint, json=put_params, headers=headers)
# print(response.text)

# delete_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{formatted_today_date}"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
