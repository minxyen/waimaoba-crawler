from waimaoba_crawler.get_company_info import get_urls
from waimaoba_crawler.get_company_info import get_company_info

import pandas as pd


start_page = input('Start From: ')
end_page = input('End at: ')

urls = get_urls(start_page, end_page)
print(len(urls))

data_list = []
for i in range(len(urls)):
    company_info = get_company_info(urls[i])
    data_list.append(company_info)

print(data_list)

df = pd.DataFrame(data_list)
print(df)
df.to_excel(f'waimaoba{start_page}-{end_page}.xlsx', index=False)


