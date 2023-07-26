import requests
import json

callsign = "Hampager.de username"
password = "Hampager.de password"  
debug = 0

def send(call,message,txgroup):
    for cs in call.split(","):
        
        data = {
            "text": message,
            "callSignNames": [cs],
            "transmitterGroupNames": [txgroup],
            "emergency": False
        }
        
        url = "http://www.hampager.de/api/calls"
        headers = {"Content-Type": "application/json"}
        auth = (callsign, password)

        response = requests.post(url, headers=headers, auth=auth, data=json.dumps(data))

        if response.ok:
            print("Message send to "+cs)
        else:
            print(f"Error sending message: {response.status_code}")
            if debug != 0:
                print(response.text)
