import json

def is_correct_json(string):
    try:
        if json.loads(string):
            return True
    except:
        return False
