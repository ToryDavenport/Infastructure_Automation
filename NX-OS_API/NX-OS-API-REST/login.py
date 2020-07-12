import requests
from pprint import pprint 
url = "https://192.168.0.253/api/mo/aaaLogin.json"

payload = "{\n\t\t\"aaaUser\": {\n\t\t\"attributes\": {\n\t\t\"name\": \"admin\",\n\t\t\"pwd\": \"Admin1234!@#$\"\n\t\t}\n\t}\n}"
headers = {
  'Content-Type': 'application/json',
  'Cookie': 'nxapi_auth=admin:jg4a64MB3LHgX292iTMuzeHJXYs=; APIC-cookie=XMdBe3N64nwHVZ+z5FT4ALgU4K/JWgwJa586xJcj0pAS6vpq1tXaocdDcerK1W3+wQslez8/UQHp0WihcJK4kH6WGsjJzTZ+h7F24L0Wr2EsqBF1sGo9p2ZXNVX+urSCnAAvguxb/yvcez47XPhMZnuliPhA/BtCSQMPvPNvzCc='
}

response = requests.post(url, headers=headers, data = payload, verify=False).json()

# pprint(response)
token = response['imdata'][0]['aaaLogin']['attributes']['token']

# pprint(token)

cookies = {}
cookies['APIC-Cookie'] = token

""" 
headers = {"content-type": "application/json"}

body = {}

int_url = ''
post_response = requests.post(int_url, data=json.dumps(body), headers=headers, cookies=cookies, verify=False).json()
print(post_response)
"""