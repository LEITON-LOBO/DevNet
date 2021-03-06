import requests
import json

meraki_api_key = input("Enter the Meraki API Key: ")
url =  "https://api.meraki.com/api/v0/organizations"
headers = {
        "X-Cisco-Meraki-API-Key": meraki_api_key,
    }
orgs = requests.get(url,headers=headers)
orgs = orgs.json()
print(json.dumps(orgs, indent=4))

for org in orgs:
    print(org['id'])
    url = "https://api.meraki.com/api/v0/organizations/"+org['id']+"/networks"
    networks = requests.get(url,headers=headers)
    networks = networks.json()
    print(json.dumps(networks, indent=4))
    for network in networks:
        print(network['id'])
        url = "https://api.meraki.com/api/v0/networks/"+network['id']+"/devices"
        devices = requests.get(url,headers=headers)
        devices = devices.json()
        print(json.dumps(devices, indent=4))
        for device in devices:
            print(device['serial'])
