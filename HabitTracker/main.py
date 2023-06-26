import requests

TOKEN = "jfnrjgbgjsmdkigm"
USERNAME = "pauly-gallagher",

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
    "token": "jfnrjgbgjsmdkigm", 
}

requests.post(url=Graph_Endpooint, json=graph_params)