

import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "data" / "inventory.txt"


def load_items():

    if not DATA_FILE.exists():
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_items(items):

    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(items, file, indent=4)


def get_next_id(items):

    if not items:
        return 1
    return max(item["id"] for item in items) + 1
