import requests
url_template = 'https://wttr.in/{}?mTq&lang=ru'

response = requests.get(url_template.format('san francisco'))
print(response.text)
response = requests.get(url_template.format('london'))
print(response.text)
response = requests.get(url_template.format('svo'))
print(response.text)
response = requests.get(url_template.format('Череповец'))
print(response.text)