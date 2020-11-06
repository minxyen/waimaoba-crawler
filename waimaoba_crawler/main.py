import logging

from waimaoba_crawler.pipeline.steps.get_urls import GetUrls
from waimaoba_crawler.pipeline.steps.get_company_info import GetCompanyInfo
from waimaoba_crawler.pipeline.steps.write_to_db import WriteToDB
from waimaoba_crawler.pipeline.steps.step import StepException
from waimaoba_crawler.pipeline.pipeline import Pipeline


def config_log():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(levelname)s:%(asctime)s:%(message)s')
    file_handler = logging.FileHandler('waimaoba.log')
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    logger.info('Log 設定已載入')


def main():
    start_page = input('Start From: ')
    end_page = input('End at: ')

    inputs = {
        'start_page': start_page,
        'end_page': end_page,
    }

    steps = [
        GetUrls(),
        GetCompanyInfo(),
        WriteToDB(),
    ]

    p = Pipeline(steps)
    p.run(inputs)


if __name__ == '__main__':
    config_log()
    main()