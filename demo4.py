import requests
import json

url = "https://imdb8.p.rapidapi.com/title/get-top-cast"

querystring = {"tconst":"tt0944947"}

headers = {
    'x-rapidapi-host': "imdb8.p.rapidapi.com",
    'x-rapidapi-key': "0eda84126fmsh4f42b4e1794706bp19167djsn88ee9428ff08"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
data=json.loads(response.text)
print(response.status_code)
for x in data:
    print(x)

