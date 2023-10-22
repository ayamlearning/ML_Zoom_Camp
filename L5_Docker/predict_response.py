import requests

url = 'http://192.168.115.44:9696/predict'

client = {
    "job": "unknown", 
    "duration": 270, 
    "poutcome": "failure"
    }

response = requests.post(url, json=client).json()
print(response)