import requests
import json


def post_numbers(numbers, addr, key):
    r = requests.post(addr + key, json=json.dumps(numbers))
    if r.status_code != 200:
        print(r.status_code, r.text)

