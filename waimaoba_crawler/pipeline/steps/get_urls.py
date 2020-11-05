import requests
from bs4 import BeautifulSoup

from .step import Step


class GetUrls(Step):
    def process(self, data, inputs):
        start_page = inputs['start_page']
        end_page = inputs['end_page']

        page_list = [page for page in range(int(start_page), int(end_page) + 1)]

        url_list = []
        for page_num in page_list:
            res = requests.get(f'http://xp.waimaoba.com/forum-23-{page_num}tm?orderby=lastpid')
            soup = BeautifulSoup(res.text, 'html.parser')
            #         print('---------------------------')
            for i in soup.find_all('li', {'class': 'media thread tap'}):
                url = f"http://xp.waimaoba.com/{i.select('a')[0].get('href')}"
                url_list.append(url)

        print('Total urls: ', len(url_list))
        print(url_list)

        return url_list
