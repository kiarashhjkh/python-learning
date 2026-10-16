import requests
import json

url = "http://api.open-notify.org/astros.json"
response = requests.get(url)
json_data = response.json()

for this_person in json_data['people']:
    print(f"{this_person['name']}", f"craft:{this_person['craft']}", sep=' | ')
    print("=============")

print(f"In total there is {json_data['number']} people in space")
