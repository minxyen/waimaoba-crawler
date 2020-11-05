from waimaoba_crawler.pipeline.steps.get_urls import GetUrls
from waimaoba_crawler.pipeline.steps.get_company_info import get_company_info
from waimaoba_crawler.pipeline.steps.write_file import write_file
from waimaoba_crawler.pipeline.steps.step import StepException
from waimaoba_crawler.pipeline.pipeline import Pipeline


def main():
    start_page = input('Start From: ')
    end_page = input('End at: ')

    inputs = {
        'start_page': start_page,
        'end_page': end_page,
    }

    steps = [
        GetUrls(),
        # GetCompanyInfo(),
        # WriteFile,
    ]

    p = Pipeline(steps)
    p.run(inputs)


if __name__ == '__main__':
    main()
