#!/usr/bin/env python

import requests

default_hostname = "127.0.0.1"
default_port = "5000"

hostname = os.getenv('INFERENCE1_SERVER_HOSTNAME', default_hostname)
port = os.getenv('INFERENCE1_SERVER_PORT', default_port)

url = f"http://{hostname}:{port}/v1/chat/completions"

headers = {
    "Content-Type": "application/json"
}

history = []

while True:
    user_message = input("> ")
    history.append({"role": "user", "content": user_message})
    data = {
        "mode": "chat",
        "character": "Example",
        "messages": history
    }

    response = requests.post(url, headers=headers, json=data, verify=False)
    assistant_message = response.json()['choices'][0]['message']['content']
    history.append({"role": "assistant", "content": assistant_message})
    print(assistant_message)
