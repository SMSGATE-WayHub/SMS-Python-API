import requests
import urllib.parse

api_key = "YourAPIkey"
sender_id = "TESTIN"
message = "YOUR MESSAGE HERE"
number = "91989xxxxxxx"  # MULTIPLE NUMBER VARIABLES PUT HERE...!

encoded_message = urllib.parse.quote_plus(message)  # encode the message content

url = f"https://www.smsgatewayhub.com/api/mt/SendSMS?APIKey={api_key}&senderid={sender_id}&channel=2&DCS=0&flashsms=0&number={number}&text={encoded_message}&route=1"

response = requests.post(url, verify=False)  # disable SSL verification

print(response.text)  # print the result of the API call
