import requests
import json

credential_file_path = 'credentials.json'

credential_file_open = open(credential_file_path, 'r')

credential_info = json.load(credential_file_open)

target_url = 'https://api.telegram.org/bot{0}/sendMessage'.format(credential_info['API_TOKEN'])

target_chat_id = credential_info['NOTIFY_USER_ID']

message_template = 'すもももももももものうち'

send_message = {'chat_id': target_chat_id, 'text': message_template}

headers = {'Content-Type': 'application/json'}

response = requests.post(url=target_url,headers=headers,data=json.dumps(send_message))

if response.ok:
  print(response.status_code)
  print(response.json())
else:
  print(response.status_code)
  print(response.json())
