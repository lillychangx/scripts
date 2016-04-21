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

   print ('payload:', payload)

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
    print ("\n")
    print (json.dumps(response.json(), sort_keys=True, indent=4))



def post_alert(access_token, client_uuid):
    # Set the request parameters
    url = "https://api.vistara.io/api/v2/tenants/" + client_uuid + "/alert"
    
    # Set proper headers
    headers = {
        "Authorization": "Bearer " + access_token,
        "Accept":"application/json",
        "Content-Type": "application/json"
        }
    
    
    payload = {
        "serviceName" : "CPU",
        "device" : {
            "hostName" : "ip-10-0-0-107",
            "resourceUUID" : "934fcbaa-8a8b-4c34-9d24-f3b78ac188cb",
            "macAddress" : "0A:57:7E:67:CF:D1",
            "ipAddress" : "ip-10-0-0-107"
            },
        "subject" : "Test Alert",
        "alertTime" : "2016-04-2016:26:00",
        "currentState" : "CRITICAL",
        "app" : "VISTARA",
        "alertType" : "Maintenance",
        "description" : "apicalls"
        }
    
    # Do the HTTP request
    response = requests.post(url, headers=headers, data=payload)
    print('Response:',response.json())
    

def update_warranty(access_token, client_uuid, resource_uuid):
    # Set the request parameters
    url = "https://api.vistara.io/api/v2/tenants/" + client_uuid + "/devices/" + resource_uuid + "/deviceWarranty"
    
    print ('url:', url)

    # Set proper headers
    headers = {
        "Authorization": "Bearer " + access_token,
        "Content-Type": "application/json",
        "Accept":"application/json",
        }


    payload = {
        "purchaseDate": "2015-11-09 12:30:00 UTC",
        "warrantyExpireDate": "2020-12-09 12:30:00 UTC"
        }

    print ('payload:', payload)
    print('json.dumps:', json.dumps(payload))



    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print ('Response Code:', response.status_code)
    print('Response:',response.json())
   


if __name__ == '__main__':

    print ("main")

    client_uuid = "client_619293"
    client_key = "zQVsBhJSSDm7CTB6JNNWTwcPTzeDfDwa"
    client_secret = "B9ENDxb67kzpDx4fGaSz5gHfRYZvJdzDsFuvuESpgEcktDEtmfRfqMGmvcH2m23j"

    
    # get access token
    access_token = get_access_token(client_key, client_secret)
    print ('access token:', access_token)
    
    # call get devices
    # get_all_devices(access_token, client_uuid)

    # call post alert
    # post_alert(access_token, client_uuid)

    # call update warranty for resource id = 934fcbaa-8a8b-4c34-9d24-f3b78ac188cb
    update_warranty(access_token, client_uuid, "934fcbaa-8a8b-4c34-9d24-f3b78ac188cb")

    
