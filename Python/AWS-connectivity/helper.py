import json

def bprint(*content):
    print(json.dumps(content, indent=4, default=str))
