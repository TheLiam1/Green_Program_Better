import requests
import json
import certifi

def values_wasserkraft():
    timestamp = requests.get("https://smard.de/app/chart_data/1226/DE/index_quarterhour.json", verify=certifi.where()).json()["timestamps"][-1]
    values = requests.get(f"https://www.smard.de/app/chart_data/1226/DE/1226_DE_quarterhour_{timestamp}.json", verify=certifi.where()).json()
    
    return values

values = values_wasserkraft()

with open("daten_wasserkraft.json", "w") as file:
    json.dump(values, file, indent=4, ensure_ascii=False)