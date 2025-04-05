import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

URL_FILES = ['cons_news.json','nonw_news.json','progr_news.json']
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


for url_file in URL_FILES:
    with open(url_file,'r') as file:
        data = json.load(file)
        
    counter = 0

    for url in data['url']:             # Websites already scraped
        if data['source'][counter] in ['foxnews.com','aljazeera.com','washingtonexaminer.com','theepochtimes.com','dailywire.com','nypost.com','jpost.com','rt.com','scmp.com','sputnikglobe.com','skynews.com.au','crikey.com.au','bangkokpost.com','chinadaily.com.cn','hurriyetdailynews.com','bbc.co.uk','nbcnews.com','time.com','globalnews.ca']:
            None
        else:
            driver.get(url)
            
            
            elements = driver.find_elements(By.TAG_NAME,'p')
            all_text = [element.text for element in elements]
            all_text = '\n'.join(all_text)
                
            article = all_text
            source = data['source'][counter]
            orientation = data['orientation']
            
            with open('news.json','r') as news_file:
                news = json.load(news_file)
                
            news['article'].append(article)
            news['source'].append(source)
            news['orientation'].append(orientation)
                
            with open('news.json', 'w') as news_file:
                json.dump(news, news_file, indent=4)
        
        counter += 1
        
        
driver.quit()
        
        
    
    
    




