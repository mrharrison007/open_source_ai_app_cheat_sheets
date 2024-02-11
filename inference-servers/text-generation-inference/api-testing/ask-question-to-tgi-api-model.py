#!/usr/bin/env python
import requests
import os
import json

default_hostname = "127.0.0.1"
default_port = "8080"

hostname = os.getenv('INFERENCE1_SERVER_HOSTNAME', default_hostname)
port = os.getenv('INFERENCE1_SERVER_PORT', default_port)

url = f"http://{hostname}:{port}/generate"

headers = {
    "Content-Type": "application/json",
}

data = {
    'inputs': 'What is your LLM model name?',
    'parameters': {
        'max_new_tokens': 300,
    },
}

response = requests.post(url, headers=headers, json=data)
response_json = response.json()

# Pretty print the JSON output
pretty_output = json.dumps(response_json, indent=4)
print(f'\n{pretty_output}')

# Parse out the generated text and print it with a blank line above
generated_text = response_json['generated_text']
print(f'\nModels reply: {generated_text}\n')