
import json
import os

def load_data():
    if os.path.exists("data/words.json"):
        with open("data/words.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open("data/words.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)