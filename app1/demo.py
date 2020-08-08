import requests
import json


url = "https://imdb8.p.rapidapi.com/title/get-most-popular-movies"

querystring = {"purchaseCountry": "India", "homeCountry": "India", "currentCountry": "India"}

headers = {
    'x-rapidapi-host': "imdb8.p.rapidapi.com",
    'x-rapidapi-key': "0eda84126fmsh4f42b4e1794706bp19167djsn88ee9428ff08"
}

response = requests.request("GET", url, headers=headers, params=querystring)
data = json.loads(response.text)
print(data)