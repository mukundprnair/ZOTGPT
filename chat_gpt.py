# this file we make the reqruest to chat and it will return a response

#API_KEY = "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"

#openai.api_key = API_KEY
import requests
import json

# Set your OpenAI API key
api_key = "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"

# Define the API endpoint URL for the chat API
api_url = "https://api.openai.com/v1/chat/completions"  # Replace with the appropriate engine URL

# Define the input parameters




# Set the headers with your API key


def chat_response(professor_data : str, user_req : str):
    content = f"This is the professor's information: {professor_data}. Here's the" \
              f"user's request: {user_req}. Generate a personalized email to the professor" \
              f"that will accomodate the request of the user."

    data = {
    "messages": [
        {"role": "system", "content": "You are helping students write academic and professional emails to professor."},
        {"role": "user", "content": content}
    ],
    "model": "gpt-3.5-turbo"
    }
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # Make a POST request to the API
    response = requests.post(api_url, data = json.dumps(data), headers = headers)

    # Check the response
    if response.status_code == 200:
        result = response.json()
        assistant_reply = result["choices"][0]["message"]["content"]
        print("Assistant's Reply:", assistant_reply)
    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.text)

    return response