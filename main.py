import requests

url_template = 'https://wttr.in/{}'
payload = {
    'mTq&lang': '',
    'lang': 'ru'
}
cities = ['Лондон', 'Шереметьево', 'Череповец']

for city in cities:
    response = requests.get(url_template.format(city), params=payload)
    response.raise_for_status()
    print(response.text)