import requests

api_key = 'thekey'
url = 'https://amplitude.com/api/2'

headers = {
    'Authorization': f'Bearer {api_key}'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("correct key")
else:
    print(f"wrong key: {response.status_code}")
