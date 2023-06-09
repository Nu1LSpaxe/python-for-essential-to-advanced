from bs4 import BeautifulSoup
import requests

# url = 'https://books.toscrape.com/catalogue/page-1.html'
# url = 'https://books.toscrape.com/catalogue/page-{}.html'

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50',
#     'Accept-Language': 'en-US,en;q=0.9',
#     'referer': 'https://www.google.com/',
# }

# response = requests.get(url)

# if response.status_code == 200:
#     content = response.text
#     soup = BeautifulSoup(content, 'html.parser')
    
#     img =  soup.find_all('img')
#     print(img)
#     for i in img:
#         alt = i.get('alt')
#         if alt: print(alt)

nameList = []

for page in range(1, 51):
    url = f'https://books.toscrape.com/catalogue/page-{page}.html'
    response = requests.get(url)

    if response.status_code == 200:
        content = response.text
        soup = BeautifulSoup(content, 'html.parser')
        
        img =  soup.find_all('img')
        print(img)
        for page in img:
            alt = page.get('alt')
            if alt: 
                nameList.append(alt)