import requests
import json

KEY = 'mykey'

MAINSTREAM_PROGRESSIVE = ['bbc.co.uk','nbcnews.com','time.com','cnn.com','globalnews.ca']

MAINSTREAM_CONSERVATIVE = ['foxnews.com', 'washingtonexaminer.com','theepochtimes.com','dailywire.com','nypost.com','jpost.com','skynews.com.au','crikey.com.au']

NON_WESTERN_MAINSTREAM = ['chinadaily.com.cn','hurriyetdailynews.com','bangkokpost.com','aljazeera.com','sputnikglobe.com']


Q = ""



for domain in MAINSTREAM_PROGRESSIVE:
    response = requests.get(url=f'https://newsapi.org/v2/everything?domains={domain}&language=en&q={Q}&apiKey={KEY}')
    responde_code = response.status_code 
    response.raise_for_status()

    articles = dict(response.json())['articles']
    
    for article in articles:
        with open('progr_news.json', 'r') as file:
            data = json.load(file)
            
        data['url'].append(article['url'])
        data['source'].append(domain)
        
        with open('progr_news.json', 'w') as file:
            json.dump(data, file, indent=4)
            

for domain in MAINSTREAM_CONSERVATIVE:
    response = requests.get(url=f'https://newsapi.org/v2/everything?domains={domain}&language=en&apiKey={KEY}')
    responde_code = response.status_code 
    response.raise_for_status()

    articles = dict(response.json())['articles']
    
    for article in articles:
        with open('cons_news.json', 'r') as file:
            data = json.load(file)
            
        data['url'].append(article['url'])
        data['source'].append(domain)
        
        with open('cons_news.json', 'w') as file:
            json.dump(data, file, indent=4)


for domain in NON_WESTERN_MAINSTREAM:
    response = requests.get(url=f'https://newsapi.org/v2/everything?domains={domain}&language=en&apiKey={KEY}')
    responde_code = response.status_code 
    response.raise_for_status()

    articles = dict(response.json())['articles']
    
    for article in articles:
        with open('nonw_news.json', 'r') as file:
            data = json.load(file)
            
        data['url'].append(article['url'])
        data['source'].append(domain)
        
        with open('nonw_news.json', 'w') as file:
            json.dump(data, file, indent=4)
