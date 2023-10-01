# Help you to read the json files and provide the JSON data

import json

def get_payload_auth():
    # Read from the auth.json file and return the json data
    file_data = open("src/constants/auth.json")
    data = json.loads(file_data)
    file_data.close()
    return data
