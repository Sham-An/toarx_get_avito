import requests
from hyper.contrib import HTTP20Adapter
s = requests.Session()
s.mount('https://', HTTP20Adapter())
r = s.get('https://www.avito.ru/', headers = go_headers)
print(r.status_code)