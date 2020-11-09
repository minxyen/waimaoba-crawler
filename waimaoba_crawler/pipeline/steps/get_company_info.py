import re
import random
import time
import logging

import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

from .step import Step


class GetCompanyInfo(Step):
    def process(self, passing_data, inputs):
        logger = logging.getLogger()
        client = MongoClient()

        company_info_list = []
        secret_key = {'e_secret_key': 'waimaoba'}
        # 'http://xp.waimaoba.com/thread-1139756.htm'
        count = 1
        for url in passing_data:
            logger.info("{0}/{1}".format(count, len(passing_data)))
            if client.waimaoba_db.company_information.count_documents({'FromURL': url}, limit=1) != 0:
                logger.info('already exists')
                count += 1
            else:
                logger.info("爬曲ing: {}".format(url))
                sleep_time = random.randint(80, 130) / 100
                time.sleep(sleep_time)
                r = requests.post(url, data=secret_key)
                if r.status_code == requests.codes.ok:
                    soup = BeautifulSoup(r.text, 'html.parser')
                    # print(soup.prettify())
                    table = soup.find_all('div', {'class': 'message break-all'})[0]
                    string = table.get_text(strip=True, separator=' ')
                    try:
                        company_name = re.search(r'Company Name \(公司名称\):(.+) Industry Category \(行业分类\)',\
                                                 string).group(1).strip()
                    except AttributeError as e:
                        logger.warning("Can't find CompanyName")
                        company_name = ''

                    try:
                        contact_person = re.search(r'Contact Person:(.+) Tel', string).group(1)
                    except AttributeError as e:
                        logger.warning("Can't find ContactPerson")
                        contact_person = ''

                    try:
                        email = re.search(r'Email Address \(电子邮件\):(.+)', string).group(1).strip()
                    except AttributeError as e:
                        logger.warning("Can't find Email")
                        email = ''

                company_info= {
                    'CompanyName': company_name,
                    'ContactPerson': contact_person,
                    'Email': email,
                    'FromURL': url,
                }

                company_info_list.append(company_info)
                count += 1

        # print(company_info_list)
        return company_info_list
