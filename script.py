import json
import time

def generate_json():
    data = {
        "users": [
            {"id": 1, "name": "Alice", "age": 25},
            {"id": 2, "name": "Bob", "age": 30},
            {"id": 3, "name": "Charlie", "age": 35}
        ]
    }

    time.sleep(2)
    
    return json.dumps(data)

if __name__ == "__main__":
    print(generate_json())