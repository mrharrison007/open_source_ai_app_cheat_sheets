import requests
import sseclient  # pip install sseclient-py
import json

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
        "mode": "instruct",
        "stream": True,
        "messages": history
    }

    # Print the data being sent to the LLM, including the history
    print("Sending the following data to the LLM:")
    print(json.dumps(data, indent=4))

    stream_response = requests.post(url, headers=headers, json=data, verify=False, stream=True)
    client = sseclient.SSEClient(stream_response)

    assistant_message = ''
    for event in client.events():
        payload = json.loads(event.data)
        chunk = payload['choices'][0]['message']['content']
        assistant_message += chunk
        print(chunk, end='')

    print()
    history.append({"role": "assistant", "content": assistant_message})

