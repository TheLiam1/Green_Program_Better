import requests
#!für Photovoltaik
import certifi

def give_right_timestamp():
    R1_TIMES_GESAMT = requests.get("https://smard.de/app/chart_data/4068/DE/index_quarterhour.json", verify=certifi.where())
    data6 = R1_TIMES_GESAMT.json()
    current_timestamp6 = data6["timestamps"][-1]
    return current_timestamp6