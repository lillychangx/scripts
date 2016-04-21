import requests

# Set the request parameters
url = "https://api.vistara.io/api/v2/tenants/client_619293/devices/search"


access_token = "1ff6ff24-f18b-47bf-bc22-62bafec35c2a"

# Set proper headers
headers = {
   "Accept":"application/json",
   "Authorization": "Bearer " + access_token
}

# Do the HTTP request
response = requests.get(url, headers=headers)
print('Response:', response.json())

