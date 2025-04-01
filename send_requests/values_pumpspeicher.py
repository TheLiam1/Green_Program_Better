import requests
import json

def values_pumpspeicher():
    timestamp = requests.get("https://smard.de/app/chart_data/4070/DE/index_quarterhour.json").json()["timestamps"][-1]
    values = requests.get(f"https://www.smard.de/app/chart_data/4070/DE/4070_DE_quarterhour_{timestamp}.json").json()
    
    return values

values = values_pumpspeicher()

with open("daten_pumpspeicher.json", "w") as file:
    json.dump(values, file, indent=4, ensure_ascii=False)