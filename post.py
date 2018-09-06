import requests
import json


def post_numbers(numbers, key):
    r = requests.post('http://127.0.0.1:7890/' + key, json=json.dumps(numbers))
    if r.status_code != 200:
        print(r.status_code, r.text)

