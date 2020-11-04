import re

import requests
from bs4 import BeautifulSoup


def get_company_info(url):
    data = {'e_secret_key': 'waimaoba'}
    # 'http://xp.waimaoba.com/thread-1139756.htm'
    r = requests.post(url, data=data)
    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text, 'html.parser')
        # print(soup.prettify())
        table = soup.find_all('div', {'class': 'message break-all'})[0]
        string = table.get_text(strip=True, separator=' ')
        try:
            company_name = re.search(r'Company Name \(公司名称\):(.+) Industry Category \(行业分类\)',\
                                     string).group(1).strip()
            print(company_name)
        except AttributeError:
            company_name = ''

        try:
            # contact_person = re.findall(r'Contact Person.+', table.text)[0].split(':')[1].strip().title()
            contact_person = re.search(r'Contact Person:(.+) Tel', string).group(1)
            print(contact_person)
        except AttributeError:
            contact_person = ''

        try:
            # email = re.findall(r'[a-zA-Z0-91\.-]+@[\w\.-]+', string)[0]
            email = re.search(r'Email Address \(电子邮件\):(.+)', string).group(1).strip()
            print(email)
        except AttributeError:
            email = ''

        print(url)
        print('------------------------------------------------------')

        return {
            'CompanyName': company_name,
            'ContactPerson': contact_person,
            'Email': email,
            'FromURL': url,
        }
