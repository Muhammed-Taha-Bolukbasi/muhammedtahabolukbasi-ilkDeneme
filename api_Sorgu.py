#ekstradan bir de görseli tarayıcıda açacak bir kod ekledim
import webbrowser
import requests
import json

url = "https://api.thecatapi.com/v1/images/search"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

if isinstance(response.text, str):

    data = json.loads(response.text)


webbrowser.open(data[0]['url'])
