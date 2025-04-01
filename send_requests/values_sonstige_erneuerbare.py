import requests
import json

def values_sonstige_erneuerbare():
    timestamp = requests.get("https://smard.de/app/chart_data/1228/DE/index_quarterhour.json").json()["timestamps"][-1]
    values = requests.get(f"https://www.smard.de/app/chart_data/1228/DE/1228_DE_quarterhour_{timestamp}.json").json()
    
    return values

values = values_sonstige_erneuerbare()

with open("daten_sonstige_erneuerbare.json", "w") as file:
    json.dump(values, file, indent=4, ensure_ascii=False)