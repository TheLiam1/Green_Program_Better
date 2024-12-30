import requests

def give_right_timestamp():
    R1_TIMES_GESAMT = requests.get("https://smard.de/app/chart_data/410/DE/index_quarterhour.json")
    data6 = R1_TIMES_GESAMT.json()
    current_timestamp6 = data6["timestamps"][-1]
    return current_timestamp6

test = give_right_timestamp()
print(test)