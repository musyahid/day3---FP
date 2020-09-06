import requests,json
from bs4 import BeautifulSoup

url = 'https://indeks.kompas.com/headline'
res = requests.get(url)
html = BeautifulSoup(res.content, 'html.parser')

headlines = html.find_all('a', class_="article__link", href=True)
response = {
    "status":res.status_code,
    "message":"Success",
    "data": []
}

for headline in headlines:
    response['data'].append({'Title': headline.text,'URL': headline['href']})

print(json.dumps(response,indent = 1))
