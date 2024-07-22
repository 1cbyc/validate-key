import requests

api_key = 'thekey'
url = 'https://amplitude.com/api/2'

headers = {
    'Authorization': f'Bearer {api_key}'
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    print("Correct key")
except requests.exceptions.HTTPError as err:
    if response.status_code == 401:
        print("Unauthorized: Invalid API key")
    else:
        print(f"HTTP error occurred: {err}")
except requests.exceptions.RequestException as err:
    print(f"Error occurred: {err}")
