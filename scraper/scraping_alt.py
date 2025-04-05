# This is scraping app is mant for those websites with "accept/decline" cookies pop ups
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException

URL_FILES = ['cons_news.json', 'nonw_news.json', 'progr_news.json']
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Open the JSON file outside the loop
with open('news.json', 'w') as news_file:
    news = {'article': [], 'source': [], 'orientation': []}
    json.dump(news, news_file, indent=4)

for url_file in URL_FILES:
    with open(url_file, 'r') as file:
        data = json.load(file)

    counter = 0

    for url in data['url']:             # Websites already scraped:
        if data['source'][counter] in ['foxnews.com', 'washingtonexaminer.com', 'theepochtimes.com',
                                       'jpost.com', 'nypost.com', 'dailywire.com', 'rt.com', 'aljazeera.com',
                                       'sputnikglobe.com', 'scmp.com', 'bbc.co.uk', 'time.com', 'nbcnews.com',
                                       'cnn.com', "chinadaily.com.cn", 'globalnews.ca']:
            counter += 1
            continue  # Skip processing URLs from these sources

        driver.get(url)

        try:
            # Wait for cookies popup and click on it
            wait = WebDriverWait(driver, 10)
            cookies_popup = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'fc-button-label')))
            cookies_popup.click()

            # Wait for presence of <p> elements
            wait = WebDriverWait(driver, 20)
            element = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'p')))
        except (TimeoutException, ElementClickInterceptedException) as e:
            print(f"Timeout or element click intercepted: {e}")
            continue  # Skip processing this URL if timeout or click interception occurs

        # Extract text from <p> elements
        elements = driver.find_elements(By.TAG_NAME, 'p')
        all_text = '\n'.join(element.text for element in elements)

        # Append data to the news JSON
        with open('news.json', 'r') as news_file:
            news = json.load(news_file)

        news['article'].append(all_text)
        news['source'].append(data['source'][counter])
        news['orientation'].append(data['orientation'])

        with open('news.json', 'w') as news_file:
            json.dump(news, news_file, indent=4)

        counter += 1

driver.quit()
