import requests

url = "https://imdb8.p.rapidapi.com/actors/get-all-videos"

querystring = {"region":"US","nconst":"nm0001667"}

headers = {
    'x-rapidapi-host': "imdb8.p.rapidapi.com",
    'x-rapidapi-key': "0eda84126fmsh4f42b4e1794706bp19167djsn88ee9428ff08"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)