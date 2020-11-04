from waimaoba_crawler.get_urls import get_urls
from waimaoba_crawler.get_company_info import get_company_info
from waimaoba_crawler.write_file import write_file


if __name__ == '__main__':
    start_page = input('Start From: ')
    end_page = input('End at: ')

    urls = get_urls(start_page, end_page)
    print("Total urls: ", len(urls))

    data_list = []
    for i in range(len(urls)):
        company_info = get_company_info(urls[i])
        data_list.append(company_info)

    write_file(data_list, start_page, end_page)


