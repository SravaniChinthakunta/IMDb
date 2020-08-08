import requests
import json

url = "https://imdb-internet-movie-database-unofficial.p.rapidapi.com/film/tt1375666"

headers = {
    'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com",
    'x-rapidapi-key': "0eda84126fmsh4f42b4e1794706bp19167djsn88ee9428ff08"
    }

response = requests.request("GET", url, headers=headers)

data=json.loads(response.text)
for k,v in data.items():
    print(k,"---",v)
