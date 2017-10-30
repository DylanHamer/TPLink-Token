"""
Generate a TP-LINK Kasa Token
by Dylan Hamer
October 30th 2017
"""

import uuid      # Generate a UUID for Client Term
import getpass   # Get password for authentication
import requests  # Send the payload

payload = """
{ 
"method": "login", 
"params": {
 "appType": "Kasa_Android",
 "cloudUserName": "{user}",
 "cloudPassword": "{passwd}", 
 "terminalUUID": "{id}"
  }
 }
"""

def authenticate()::
    username = input(" Please enter a username: ")
    password = getpass.getpass(" Please enter a password: ")
    return username, password

def sendPayload(username, password, termUUID):
    payload = payload.format(user=username, passwd=password, id=termUUID)
    response = requests.post(url, json=payload)
    return response.json
    
    
def main():
    print("Authenticating...")
    username, password = authenticate()
    print("Generating UUID...")
    termUUID = uuid.uuid4()
    print(" UUID Version 4 is: " + termUUID)
    print("Sending payload...")
    response = sendPayload(username, passwors, termUUID)
    print(" Response from server:")
    print(" "+response)
    