import requests


post_params = {
    "token" : "jfnrjgbgjsmdkigm",
    "username" : "pauly-gallagher",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

Pixela_Endpoint = "https://pixe.la/v1/users"

response =requests.post(url=Pixela_Endpoint, json=post_params)
print(response.text)