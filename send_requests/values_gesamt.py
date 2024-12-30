import times_gesamt as mtg
import requests
import json

current_timestamp7 = mtg.give_right_timestamp()

def get_data_out_of_r1_gesamt_json(current_time):
    R2_GESAMT = requests.get(f"https://www.smard.de/app/chart_data/410/DE/410_DE_quarterhour_{current_time}.json")
    data8 = R2_GESAMT.json()
    return data8

test = get_data_out_of_r1_gesamt_json(current_timestamp7)
print(json.dumps(test, indent=4))