import requests
parameters = []
url = "https://indiadataportal.com/soil_Codebook"

headers = {
    'cache-control': "no-cache",
    'postman-token': "f41b6b09-5921-b4ee-b60a-b4b162cc0cfa"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)