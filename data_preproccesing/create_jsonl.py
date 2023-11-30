import json
"""write the jsonL file"""


def create_json(data_dict):
    with open("train.jsonl", "w") as f:
        for line in data_dict:
            f.write(json.dumps(line) + "\n")