import os
import json
import subprocess
import requests

def generate(diff, model, prompt):
    data={
        "model": model,
        "prompt": "{prompt}".format(prompt=prompt),
    }
    response = requests.post("http://localhost:11434/api/generate", json=data)
    json_strings = response.text.strip().split('\n')
    responses = [json.loads(js)["response"] for js in json_strings]
    result = "".join(responses)

    return result