import requests

TOKEN = "jfnrjgbgjsmdkigm"
USERNAME = "pauly-gallagher"
ID = "portuguese"

post_params = {
    "token" : "jfnrjgbgjsmdkigm",
    "username" : "pauly-gallagher",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

Pixela_Endpoint = "https://pixe.la/v1/users"
Graph_Endpooint = f"{Pixela_Endpoint}/{USERNAME}/graphs"



# response =requests.post(url=Pixela_Endpoint, json=post_params)
# print(response.text)

graph_params = {
    "id": "portuguese",
    "name" : "Rastreador_de_habitos",
    "unit" : "minutes",
    "type" : "int",
    "color" : "ajisai",
}

headers= {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=Graph_Endpooint, json=graph_params, headers=headers)
# response.raise_for_status()
# print(response)

Post_Pixal = f"{Graph_Endpooint}/{ID}"

pixal_params = {
    "date" : "20230627",
    "quantity" : "45",
}

response = requests.post(url=Post_Pixal, json=pixal_params, headers=headers)
print(response.text)