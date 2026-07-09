import json
import os

HISTORY_FILE = "history.json"

def save_history(event, themes, starters, feedback=None):
    record = {
        "event": event,
        "themes": themes,
        "starters": starters,
        "feedback": feedback
    }

    history = []

    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as file:
            try:
                history = json.load(file)
            except json.JSONDecodeError:
                history = []

    history.append(record)

    with open(HISTORY_FILE, "w") as file:
        json.dump(history, file, indent=4)

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as file:
            return json.load(file)
    return []
