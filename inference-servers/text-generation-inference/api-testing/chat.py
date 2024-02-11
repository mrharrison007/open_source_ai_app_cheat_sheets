import requests
import os

# if not a INFERENCE1_SERVER_HOSTNAME environment variable is set, use the default value
# if not a INFERENCE1_SERVER_PORT environment variable is set, use the default value

default_hostname = "127.0.0.1"
default_port = "8080"

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

    try:
        # Adding timeout for the request to avoid hanging indefinitely
        response = requests.post(url, headers=headers, json=data, verify=False, timeout=10)

        # Check if response was successful
        response.raise_for_status()

        # Attempt to parse JSON response
        try:
            assistant_message = response.json()['choices'][0]['message']['content']
            history.append({"role": "assistant", "content": assistant_message})
            print(assistant_message)
        except KeyError as e:
            # If the expected keys aren't in the JSON response
            print(f"Key error: {e}. Response might not contain expected data.")
            print("Response JSON:", response.json())
        except ValueError:
            # If response body does not contain valid JSON
            print("Invalid JSON in response")

    except requests.exceptions.HTTPError as errh:
        print ("Http Error:",errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
    except requests.exceptions.RequestException as err:
        print ("Oops: Something Else",err)

