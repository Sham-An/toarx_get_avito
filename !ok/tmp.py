from urllib.parse import urlparse

import pandas as pd


def url_parser(url):

    parts = urlparse(url)
    directories = parts.path.strip('/').split('/')
    queries = parts.query.strip('&').split('&')

    elements = {
        'scheme': parts.scheme,
        'netloc': parts.netloc,
        'path': parts.path,
        'params': parts.params,
        'query': parts.query,
        'fragment': parts.fragment,
        'directories': directories,
        'queries': queries,
    }

    return elements
def url_components_to_df(df, url='url'):
    """Parses a dataframe of URLs and returns a dataframe of URL components.

    Args:
        df (object): Pandas dataframe containing URLs.
        url (string, optional): Optional name of column containing URL, if not 'url'.

    Return:
        df (object): Pandas dataframe containing URL components.
    """

    df_output = pd.DataFrame(columns=['scheme', 'netloc', 'path',
                                      'params', 'query', 'fragment',
                                      'directories', 'queries'])

    for index, row in df.iterrows():
        elements = url_parser(row['url'])

        page = {
            'scheme': elements['scheme'],
            'netloc': elements['netloc'],
            'path': elements['path'],
            'params': elements['params'],
            'query': elements['query'],
            'fragment': elements['fragment'],
            'directories': elements['directories'],
            'queries': elements['queries'],
        }

        df_output = df_output.append(page, ignore_index=True)

    return df_output


if __name__ == "__main__":

    url = "http://flyandlure.org/articles/fly_fishing/fly_fishing_diary_july_2020?q=word&b=something#anchor"

    urls = [
        'https://www.google.com/search?q=how+to+dispose+of+a+corpse&oq=how+to+dispose+of+a+corpse&aqs=chrome..69i57j69i64.4925j1j7&sourceid=chrome&ie=UTF-8',
        'https://tales.as/101-things-to-do-with-a-dead-body_9780997711639?utm_source=google-shopping&utm_medium=cpc&utm_campaign=',
        'https://www.worldofbooks.com/en-gb/books/hugh-whitemore/disposing-of-the-body/9781872868271#NGR9781872868271',
        'https://www.google.com/search?q=where+to+buy+hydrofluoric+acid&oq=where+to+buy+hydrofl&aqs=chrome.1.69i57j0l2j0i10j0i10i395j0i395i457j0i10i395l2.8058j1j7&sourceid=chrome&ie=UTF-8'
    ]

    elements = url_parser(url)

    df_output = url_components_to_df(url)#(df_sitemap)
    df_output.tail()

    #UPDATE table1 SET name = ‘Людмила Иванова’ WHERE id = 2;
