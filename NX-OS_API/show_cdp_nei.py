import requests

url = "http://192.168.0.253:80/ins"

payload = "{
            "ins_api": {
            "version":"1.0",
            "type": "cli_show",
            "chunk": "0",
            "sid":"1",
            "input":"show run",
            "output_format":"json"
            }
        }"



headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic YWRtaW46YWRtaW4=',
  'Cookie': 'nxapi_auth=admin:159448523198363176'
}

response = requests.POST(url, headers=headers, data = payload)

print(response.text.encode('utf8'))

