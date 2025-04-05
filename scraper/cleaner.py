import json

with open('news_clean.json','r') as file:
        data = json.load(file)


for n in range(len(data['article'])):
    if data['article'][n] != '':
        with open('news.json','r') as temp_file:
            new_data = json.load(temp_file)

        new_data['article'].append(data['article'][n])
        new_data['source'].append(data['source'][n])
        new_data['orientation'].append(data['orientation'][n])
        
        with open('news.json', 'w') as temp_file:
            json.dump(new_data, temp_file, indent=4)

