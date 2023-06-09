from bs4 import BeautifulSoup
import requests

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50',
    'Accept-Language': 'en-US,en;q=0.9',
    'referer': 'https://www.google.com/',
    # 'cookie': 'over18=1'
}

session = requests.session()
session.cookies.set('over18', '1')
response = session.get(url)

if response.status_code == 200:
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')
    div = soup.find_all('div', class_='title')
    
    for i in div:
        print(i.get_text())