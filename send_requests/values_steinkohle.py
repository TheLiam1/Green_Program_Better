import requests
import json
import certifi

def values_steinkohle():
    timestamp = requests.get("https://smard.de/app/chart_data/4069/DE/index_quarterhour.json", verify=certifi.where()).json()["timestamps"][-1]
    values = requests.get(f"https://www.smard.de/app/chart_data/4069/DE/4069_DE_quarterhour_{timestamp}.json", verify=certifi.where()).json()
    
    return values

values = values_steinkohle()

with open("daten_steinkohle.json", "w") as file:
    json.dump(values, file, indent=4, ensure_ascii=False)