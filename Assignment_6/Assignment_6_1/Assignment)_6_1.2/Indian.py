import json


states = {
    "Andhra Pradesh": "Amaravati",
    "Assam": "Dispur",
    "Bihar": "Patna",
    "Gujarat": "Gandhinagar",
    "Haryana": "Chandigarh",
    "Karnataka": "Bengaluru",
    "Maharashtra": "Mumbai"
}

with open("indian_states.json", "w") as f:
    json.dump(states, f)

