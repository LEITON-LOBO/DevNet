import requests
import json

meraki_api_key = input("Enter the Meraki API Key: ")
ntwID= input("Enter the Network ID: ")
url =  "https://api.meraki.com/api/v0/networks/"+ntwID+"/devices"
headers = {
        "X-Cisco-Meraki-API-Key": meraki_api_key,
    }
devices = requests.get(url,headers=headers)
print(json.dumps(devices.json(), indent=4))
