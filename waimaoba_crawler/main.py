import re

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


def get_company_info():
    urls = get_urls()

    for url in urls:
        data = {'e_secret_key': 'waimaoba'}
        # 'http://xp.waimaoba.com/thread-1139756.htm'
        r = requests.post(url, data=data)
        if r.status_code == requests.codes.ok:
            soup = BeautifulSoup(r.text, 'html.parser')
            # print(soup.prettify())

            try:
                table = soup.find_all('div', {'class': 'message break-all'})[0]
                Company = re.findall(r'Company Name \(公司名称\): .+ Industry',\
                                     table.get_text(strip=True, separator=' '))[0][:-9].split(':')[1].strip().upper()
                print(Company)

                ContactPerson = re.findall(r'Contact Person.+', table.text)[0].split(':')[1].strip().title()
                print(ContactPerson)

                Email = re.findall(r'[a-zA-Z0-91\.-]+@[\w\.-]+', table.text)[0]
                print(Email)
                print(url)
                print('------------------------------------------------------')

            except IndexError as e:
                print(e, '->', url)
                print('------------------------------------------------------')


get_company_info()