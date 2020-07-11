curl --location --request POST 'http://192.168.0.253:80/ins' \
--header 'Content-Type: application/json' \
--header 'Authorization: Basic YWRtaW46YWRtaW4=' \
--header 'Cookie: nxapi_auth=admin:159448523198363176' \
--data-raw '{
  "ins_api": {
    "version": "1.2",
    "type": "cli_show",
    "chunk": "0",
    "sid": "1",
    "input": "show cdp nei ",
    "output_format": "json"
  }
}'
