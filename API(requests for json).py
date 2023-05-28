import json
import requests

arr_icao = input("Enter ICAO \n>>")

params = {"access_key": 'a2824f8004d5a49d6c5118a51214a95e',"arr_icao": arr_icao,"limit": 100}
print("collecting the data from the API ")
api_result = requests.get('http://api.aviationstack.com/v1/flights', params)

with open("GI.json", "w") as file:
    json.dump(api_result.json(), file, indent=4)

print("The Data stored in the file <<<<<<[GI.json]>>>>>>")
