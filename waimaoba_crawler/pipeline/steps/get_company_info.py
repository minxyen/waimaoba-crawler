import re

import requests
from bs4 import BeautifulSoup

from .step import Step


class GetCompanyInfo(Step):
    def process(self, passing_data, inputs):

        company_info_list = []
        secret_key = {'e_secret_key': 'waimaoba'}
        # 'http://xp.waimaoba.com/thread-1139756.htm'
        for url in passing_data:
            r = requests.post(url, data=secret_key)
            if r.status_code == requests.codes.ok:
                soup = BeautifulSoup(r.text, 'html.parser')
                # print(soup.prettify())
                table = soup.find_all('div', {'class': 'message break-all'})[0]
                string = table.get_text(strip=True, separator=' ')
                try:
                    company_name = re.search(r'Company Name \(公司名称\):(.+) Industry Category \(行业分类\)',\
                                             string).group(1).strip()
                    print('CompanyName: ', company_name)
                except AttributeError:
                    print('None')
                    company_name = ''

                try:
                    # contact_person = re.findall(r'Contact Person.+', table.text)[0].split(':')[1].strip().title()
                    contact_person = re.search(r'Contact Person:(.+) Tel', string).group(1)
                    print('ContactPerson: ', contact_person)
                except AttributeError:
                    print('None')
                    contact_person = ''

                try:
                    # email = re.findall(r'[a-zA-Z0-91\.-]+@[\w\.-]+', string)[0]
                    email = re.search(r'Email Address \(电子邮件\):(.+)', string).group(1).strip()
                    print('Email: ', email)
                except AttributeError:
                    print('None')
                    email = ''

            print('FromUrl: ', url)
            print('------------------------------------------------------')

            company_info= {
                'CompanyName': company_name,
                'ContactPerson': contact_person,
                'Email': email,
                'FromURL': url,
            }

            company_info_list.append(company_info)

        print(company_info_list)
        return company_info_list
