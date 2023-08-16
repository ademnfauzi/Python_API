import requests
import json

# set the API endpoint and query parameters
endpoint = "https://official-joke-api.appspot.com/random_joke"
params = {"param1": "value1", "param2": "value2"}

# make the API request
response = requests.get(endpoint)

# check the response status code
if response.status_code == 200:
    # the request was successful
    data = response.json()
    # do something with the response data   
    with open('data.txt', 'w') as file:
        json.dump(data, file, indent=4)

    print("Success")
else:
    # the request failed
    print(f"Error {response.status_code} : {response.text}")
