# Need to install requests package for python
# sudo easy_install requests
import requests
import json


def get_access_token(client_key, client_secret):
   # Set the request parameters
   url = "https://api.vistara.io/auth/oauth/token"
   
   # Set proper headers
   headers = {"Accept":"application/json"}
   
   # Do the HTTP request
   payload = {
       "client_id": client_key,
       "client_secret": client_secret,
       "grant_type": "client_credentials",
   }

   
   response = requests.post(url, data=payload, headers=headers)

   
   # Check for HTTP code 200
   if response.status_code == 200: 
       # Decode the JSON response into a dictionary and use the data
       # print('Response:',response.json())
       return response.json()['access_token']
   else:
       return ""


def get_all_devices(access_token, client_uuid):
    # Set the request parameters
    url = "https://api.vistara.io/api/v2/tenants/" + client_uuid + "/devices/search"

    
    # Set proper headers
    headers = {
        "Accept":"application/json",
        "Authorization": "Bearer " + access_token
        }

    # Do the HTTP request
    response = requests.get(url, headers=headers)
 #   print('Response:', response.json())
    
    device_data = response.json()
    
    print ("\n")
#    print (json.dumps(device_data, sort_keys=True, indent=4))
#    print ("\n")

    for device in device_data['results']:
       print ("device id: ", device['id'], "device name: ", device['generalInfo']['hostName'])
       print ("\n")



if __name__ == '__main__':

   client_uuid = "client_619293"
   client_key = "zQVsBhJSSDm7CTB6JNNWTwcPTzeDfDwa"
   client_secret = "B9ENDxb67kzpDx4fGaSz5gHfRYZvJdzDsFuvuESpgEcktDEtmfRfqMGmvcH2m23j"

   
    # get access token
   access_token = get_access_token(client_key, client_secret)
    # print ('access token:', access_token)
   
    # call get devices
   get_all_devices(access_token, client_uuid)


    
