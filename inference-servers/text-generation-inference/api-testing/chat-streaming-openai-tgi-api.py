#!/usr/bin/env python
from openai import OpenAI
import os
import json

default_hostname = "127.0.0.1"
default_port = "8080"

hostname = os.getenv('INFERENCE1_SERVER_HOSTNAME', default_hostname)
port = os.getenv('INFERENCE1_SERVER_PORT', default_port)

url = f"http://{hostname}:{port}/v1"

# init the client but point it to TGI
client = OpenAI(
    base_url=url,
    api_key="-"
)

chat_completion = client.chat.completions.create(
    model="tgi",
    messages=[
        {"role": "system", "content": "You are a helpful assistant." },
        {"role": "user", "content": "What is deep learning?"}
    ],
    stream=True
)

# iterate and print stream
for message in chat_completion:
    print(message)