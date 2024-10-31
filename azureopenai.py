import os, requests, uuid, json, config

# Don't forget to replace with your Azure OpenAI subscription key!
# If you prefer to use environment variables, see Extra Credit for more info.
apikey = config.openai_key
endpoint = config.openai_endpoint

# Our Flask route will supply two arguments: prompt and chat_history.
# When the send message button is pressed in our Flask app, the Ajax request
# will grab these values from our web app, and use them in the request.
# See main.js for Ajax calls.



def get_openai_response(chat_history=[]):


    headers = {
        "Content-Type": "application/json",
        "api-key": apikey,
    }

    payload = {
    "messages": chat_history,
    "temperature": 0.7,
    "top_p": 0.95,
    "max_tokens": 800
    }

    # Send request
    try:
        response = requests.post(endpoint, headers=headers, json=payload)
        response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
    except requests.RequestException as e:
        raise SystemExit(f"Failed to make the request. Error: {e}")

    # Handle the response as needed (e.g., print or process)
    return(response.json())

# Example usage:
# print(get_openai_response()['choices'][0]['message']['content'])