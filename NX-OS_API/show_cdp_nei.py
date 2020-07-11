import requests

url = "http://192.168.0.253:80/ins"

payload = "{\n  \"ins_api\": {\n    \"version\": \"1.2\",\n    \"type\": \"cli_show\",\n    \"chunk\": \"0\",\n    \"sid\": \"1\",\n    \"input\": \"show cdp nei \",\n    \"output_format\": \"json\"\n  }\n}"
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic YWRtaW46YWRtaW4=',
  'Cookie': 'nxapi_auth=admin:159448523198363176'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))

