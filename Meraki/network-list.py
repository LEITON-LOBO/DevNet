import requests
import json

meraki_api_key = input("Enter the Meraki API Key: ")
orgID= input("Enter the Organization ID: ")
url =  "https://api.meraki.com/api/v0/organizations/"+orgID+"/networks"
headers = {
        "X-Cisco-Meraki-API-Key": meraki_api_key,
    }
networks = requests.get(url,headers=headers)
print(json.dumps(networks.json(), indent=4))
