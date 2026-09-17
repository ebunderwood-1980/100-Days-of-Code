import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "ebunderwood"
TOKEN = "d03He0wm1XW2RwfiHDOZ8PyKqqbDJO3DqIRT"
graph_id = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Commenting this out becuase the use has already been created on first successful
# running of the program.
# pixela_response = requests.post(url=pixela_endpoint, json=user_params)
# print(pixela_response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}"

# graph_config = {
#     "id": "graph1",
#     "name": "My Cycling Graph",
#     "unit": "km",
#     "type": "float",
#     "color": "ajisai",
# }

today = datetime.now()


graph_config = {
    "date": today.strftime("%Y%m%d"),  # Uses datetime module
    "quantity": "5",
}

# ---------- Requests Headers ----------

headers = {
    "X-USER-TOKEN": TOKEN,
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)
