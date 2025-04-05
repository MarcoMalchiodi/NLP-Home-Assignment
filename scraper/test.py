# The purpose of this file is solely for checking purposes
import requests
import json

KEY = 'mykey'

response = requests.get(url=f'https://newsapi.org/v2/everything?domains=cnn.com&language=en&q=elections&apiKey={KEY}')
responde_code = response.status_code 
response.raise_for_status()

articles = dict(response.json())['articles']

#print(len(articles))


with open('news.json','r') as file:
    data = json.load(file)
    
counter1 = 0
counter2 = 0
counter3 = 0

for pol in data['orientation']:
    if pol == "western_conservative":
        counter1 += 1
    elif pol == 'non_western':
        counter2 += 1
    else:
        counter3 += 1
        
'''print(counter1)
print(counter2)
print(counter3)'''

'''print(len(data['article']))
print(len(data['source']))
print(len(data['orientation']))'''