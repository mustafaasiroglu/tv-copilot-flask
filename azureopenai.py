import os, requests, uuid, json, config


def get_openai_response(chat_history=[]):

    headers = {
        "Content-Type": "application/json",
        "api-key": config.openai_key,
    }

    payload = {
    "messages": chat_history,
    "temperature": 0.7,
    "top_p": 0.95,
    "max_tokens": 800
    }

    # Send request
    try:
        response = requests.post(config.openai_endpoint, headers=headers, json=payload)
        response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
    except requests.RequestException as e:
        raise SystemExit(f"Failed to make the request. Error: {e}")

    # Handle the response as needed (e.g., print or process)
    return(response.json())

# Example usage:
# print(get_openai_response()['choices'][0]['message']['content'])

def get_promptflow_response(requestbody):

    endpoint = "https://tv-copilot.swedencentral.inference.ml.azure.com/score"

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + config.promptflow_key,
        "azureml-model-deployment":config.promptflow_deployment
    }

    payload = requestbody
    # Send request
    try:
        response = requests.post(config.promptflow_endpoint, headers=headers, json=payload)
        response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
    except requests.RequestException as e:
        raise SystemExit(f"Failed to make the request. Error: {e}")

    # Handle the response as needed (e.g., print or process)
    return(response.json())