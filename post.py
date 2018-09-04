import requests
import json

global_key = "wslS32bnkb29n1sakSDB3189930SSNssdhH84"


def post_numbers(numbers):
    r = requests.post('http://127.0.0.1:7890/' + global_key, json=json.dumps(numbers))
    if r.status_code != 200:
        print(r.status_code, r.text)

