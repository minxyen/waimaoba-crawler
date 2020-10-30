import re

import requests
from bs4 import BeautifulSoup


data = {'e_secret_key': 'waimaoba'}
r = requests.post('http://xp.waimaoba.com/thread-1139756.htm', data=data)
if r.status_code == requests.codes.ok:
    soup = BeautifulSoup(r.text, 'html.parser')
    # print(soup.prettify())

    table = soup.find_all('div', {'class': 'message break-all'})[0]
    Company = re.findall(r'Company Name \(公司名称\): .+ Industry', table.get_text(strip=True, separator=' '))[0][:-9].split(':')[1].strip().upper()
    print(Company)

    ContactPerson = re.findall(r'Contact Person.+', table.text)[0].split(':')[1].strip().title()
    print(ContactPerson)

    Email = re.findall(r'[a-zA-Z0-9\.-]+@[\w\.-]+', table.text)[0]
    print(Email)