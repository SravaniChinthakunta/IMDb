import json
import requests

url = "https://imdb-internet-movie-database-unofficial.p.rapidapi.com/search/inception"

headers = {
    'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com",
    'x-rapidapi-key': "0eda84126fmsh4f42b4e1794706bp19167djsn88ee9428ff08"
    }

response = requests.request("GET", url, headers=headers)

data = json.loads(response.text)
for x,y in data.items():
    print(x,'=======',y)
import requests

url = "https://imdb8.p.rapidapi.com/title/get-most-popular-movies"

querystring = {"purchaseCountry":"US","homeCountry":"US","currentCountry":"US"}

headers = {
    'x-rapidapi-host': "imdb8.p.rapidapi.com",
    'x-rapidapi-key': "0eda84126fmsh4f42b4e1794706bp19167djsn88ee9428ff08"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)