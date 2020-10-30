import re

import requests
from bs4 import BeautifulSoup

from waimaoba_crawler.get_urls import get_urls


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
