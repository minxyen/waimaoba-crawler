import pandas as pd


def write_file(data_list, start_page, end_page):
    df = pd.DataFrame(data_list)
    print(df)
    df.to_excel(f'waimaoba{start_page}-{end_page}.xlsx', index=False)