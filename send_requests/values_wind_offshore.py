import requests
import json
import certifi

def values_wind_offshore():
    timestamp = requests.get("https://smard.de/app/chart_data/1225/DE/index_quarterhour.json", verify=certifi.where()).json()["timestamps"][-1]
    values = requests.get(f"https://www.smard.de/app/chart_data/1225/DE/1225_DE_quarterhour_{timestamp}.json", verify=certifi.where()).json()
    
    return values

values = values_wind_offshore()

with open("daten_wind_offshore.json", "w") as file:
    json.dump(values, file, indent=4, ensure_ascii=False)