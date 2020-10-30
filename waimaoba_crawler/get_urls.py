import requests
from bs4 import BeautifulSoup


def get_urls():
    start_page = input('Start From: ')
    end_page = input('End at: ')
    page_list = []
    for page in range(int(start_page), int(end_page) + 1):
        # print(page)
        page_list.append(page)

    urls = []
    for page_num in page_list:
        res = requests.get(f'http://xp.waimaoba.com/forum-23-{page_num}tm?orderby=lastpid')
        soup = BeautifulSoup(res.text, 'html.parser')
        #         print('---------------------------')
        for i in soup.find_all('li', {'class': 'media thread tap'}):
            url = f"http://xp.waimaoba.com/{i.select('a')[0].get('href')}"
            urls.append(url)

    print(len(urls))
    return urls
