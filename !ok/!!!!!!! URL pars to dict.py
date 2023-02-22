from urllib.parse import urlparse
import urllib
#decode utf-8 decode utf8 = urllib.parse.unquote(TEXT, encoding='utf-8', errors='replace')

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


def main():

    url_path = 'https://www.avito.ru/tarasovskiy/zapchasti_i_aksessuary?cd=1&d=1&q=%D1%81%D0%BA%D1%83%D1%82%D0%B5%D1%80'
    pars_dump = url_parser(url_path)
    scheme = pars_dump['scheme']  #'scheme': 'https'
    netloc = pars_dump['netloc']  #'netloc': 'www.avito.ru'
    path = pars_dump['path']      #'path': '/tarasovskiy/zapchasti_i_aksessuary'
    params = pars_dump['params']  # 'params': ''
    query = pars_dump['query']#'query': 'cd=1&d=1&q=%D1%81%D0%BA%D1%83%D1%82%D0%B5%D1%80'
    #urllib2.unquote('test.org/%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9%20%D1%82%D0%B5%D0%BA%D1%81%D1%82')
    query_str_decode = urllib.parse.unquote(query, encoding='utf-8', errors='replace')
    #urllib.parse.unquote(string, encoding='utf-8', errors='replace')
    print(f'decode {query_str_decode}')
    fragment = pars_dump['fragment'] #'fragment': ''
    directories = pars_dump['directories'] #'directories': ['tarasovskiy', 'zapchasti_i_aksessuary']
    queries = pars_dump['queries'] #'queries': ['cd=1', 'd=1', 'q=%D1%81%D0%BA%D1%83%D1%82%D0%B5%D1%80']
    print(query) ##.decode('utf8')  text.encode('cp1251')
    url_city = directories[0]
    url_path = directories[1]
    url_from_dict = (f'{scheme}://{netloc}/{url_city}/{url_path}?{query_str_decode}')
    print(url_from_dict)
    print(pars_dump)


if __name__ == '__main__':
    main()
