import json
import random
import csv
import sys
from uuid import uuid4

# Define human inputs
human_inputs = [
    "You are an AI agent tasked with playing Super Mario brothers. What is the best move?",
    "Given this frame from Super Mario World, what is the best button to press?",
    "As an AI, how would you navigate through this level?",
    "Imagine you're controlling a character in a game. What actions would you take?",
    "If you were an AI player, what would be your next move?",
    "You're in control of a game character. What input would you provide at this moment?"
]

def filter_true_buttons(movie_input):
    return {key: value for key, value in movie_input.items() if value}

def generate_unique_id():
    return str(uuid4())

def create_json_object(filename, true_buttons, selected_human_input):
    return {
        "id": generate_unique_id(),  
        "image": filename,  
        "conversations": [
            {
                "from": "human",
                "value": selected_human_input  
            },
            {
                "from": "gpt",
                "value": json.dumps(true_buttons, indent=4)  
            }
        ]
    }

def convert_csv_to_json(input_csv, output_json):
    json_data_list = []
    with open(input_csv, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        next(reader)  # Skip header
        for row in reader:
            filename = row[0].split('data\\')[-1]
            movie_input = json.loads(row[2])
            true_buttons = filter_true_buttons(movie_input)
            selected_human_input = random.choice(human_inputs)
            json_data = create_json_object(filename, true_buttons, selected_human_input)
            json_data_list.append(json_data)

    with open(output_json, 'w') as jsonfile:
        json.dump(json_data_list, jsonfile, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_csv> <output_json>")
        sys.exit(1)
    input_csv = sys.argv[1]
    output_json = sys.argv[2]
    convert_csv_to_json(input_csv, output_json)