import pandas as pd
from pymongo import MongoClient

from .step import Step


class WriteToDB(Step):
    def process(self, passing_data, inputs):
        client = MongoClient()
        for single_data in passing_data:
            client.waimaoba_db.company_information.insert_one(single_data)

# def write_file(data_list, start_page, end_page):
#     df = pd.DataFrame(data_list)
#     print(df)
#     df.to_excel(f'waimaoba{start_page}-{end_page}.xlsx', index=False)


