import re

import requests
from bs4 import BeautifulSoup

from waimaoba_crawler.get_urls import get_urls


def get_company_info(url):
    data = {'e_secret_key': 'waimaoba'}
    # 'http://xp.waimaoba.com/thread-1139756.htm'
    r = requests.post(url, data=data)
    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text, 'html.parser')
        # print(soup.prettify())
        try:
            table = soup.find_all('div', {'class': 'message break-all'})[0]
            company_name = re.findall(r'Company Name \(公司名称\): .+ Industry',\
                                 table.get_text(strip=True, separator=' '))[0][:-9].split(':')[1].strip().upper()
            print(company_name)
        except IndexError:
            company_name = ''

        try:
            contact_person = re.findall(r'Contact Person.+', table.text)[0].split(':')[1].strip().title()
            print(contact_person)
        except IndexError:
            contact_person = ''

        try:
            email = re.findall(r'[a-zA-Z0-91\.-]+@[\w\.-]+', table.text)[0]
            print(email)
        except IndexError:
            email = ''

        print(url)
        print('------------------------------------------------------')

        return {
            'CompanyName': company_name,
            'ContactPerson': contact_person,
            'Email': email,
            'FromURL': url,
        }
