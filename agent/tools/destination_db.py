# load and filter data from the JSON file :

import json
from typing import List, Dict


def load_destinations() -> List[Dict]:   
    with open("data/destinations.json", "r") as f:       # Loads all destination data from the JSON file 
        return json.load(f)


def filter_destinations(preferences: Dict) -> List[Dict]:
    all_destinations = load_destinations()                  # Filters destinations based on user preferences
    filtered = []

    for dest in all_destinations:
        match = True

        if "interest" in preferences:
            if preferences["interest"].lower() not in dest.get("tags", []):
                match = False

        if "region" in preferences:
            if preferences["region"].lower() != dest.get("region", "").lower():
                match = False

        if "budget" in preferences:
            if preferences["budget"].lower() != dest.get("budget", "").lower():
                match = False

        if match:
            filtered.append(dest)

    return filtered
