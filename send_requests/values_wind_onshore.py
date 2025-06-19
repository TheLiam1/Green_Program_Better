import requests
import json
import certifi

def values_wind_onshore():
    timestamp = requests.get("https://smard.de/app/chart_data/4067/DE/index_quarterhour.json", verify=certifi.where()).json()["timestamps"][-1]
    values = requests.get(f"https://www.smard.de/app/chart_data/4067/DE/4067_DE_quarterhour_{timestamp}.json", verify=certifi.where()).json()
    
    return values

values = values_wind_onshore()

with open("daten_wind_onshore.json", "w") as file:
    json.dump(values, file, indent=4, ensure_ascii=False)