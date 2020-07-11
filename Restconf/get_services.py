import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Set up connection parameters in a dictionary
router = {"ip": "192.168.0.254", "port": "443",
          "user": "cisco", "password": "cisco"}

# Set the REST API headers
headers = {"Accept": "application/yang-data+json",
           "Content-Type": "application/yang-data+json"}

url = f"https://{router['ip']}:{router['port']}/restconf/data/tailf-ncs:services"

# Supress credential warning for this exercise
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
response = requests.get(url, headers=headers, auth=(
    router['user'], router['password']), verify=False)

api_data = response.json()
print("/" * 50)
print(api_data)


