import requests
import sys
import json

HOST='devasc-iosxe-mgmt-2.cisco.com:443/restconf'
USER='developer'
PASS='CactusMopedGreen42'

# Disable SSL warning
requests.packages.urllib3.disable_warnings()

# Basic Auth is used for authentication.
def get_configured_interfaces(interface):
    """Retrieving config data (interface) from RESTCONF API."""
    api = "/restconf/data/ietf-interfaces:interfaces/interface="+interface
    url = "https://"+HOST+api
    # RESTCONF media types for REST API headers
    headers = {'Content-Type': 'application/yang-data+json',
               'Accept': 'application/yang-data+json'}
    # this statement performs a GET on the specified url
    response = requests.get(url, auth=(USER, PASS),headers=headers, verify=False)
    print("Status code: ",response.status_code)
    if response.status_code == 200:
        # return JSON
        return response
    else:
        return None

def main():
    """Simple main method calling function."""
    interface = "GigabitEthernet1"
    interfaces = get_configured_interfaces(interface)
    # print the json that is returned
    if interfaces!= None:
        response_json = interfaces.json()
        print("Response:",json.dumps(response_json,indent = 4))
    else:
        print("Looks like "+interface+" is not configured !!!")

if __name__ == '__main__':
    sys.exit(main())
