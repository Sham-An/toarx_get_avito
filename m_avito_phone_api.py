# FROM https://github.com/viktor-gorinskiy/avito/blob/main/main.py
import requests, json, sys

key = 'af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir' # ключ, с которым всё работает, не разбирался где его брать, но похоже он статичен, т.к. гуглится на различных форумах
cookie_old = '__cfduid=da6b6b5b9f01fd022f219ed53ac3935791610912291; sessid=ef757cc130c5cd228be88e869369c654.1610912291; _ga=GA1.2.559434019.1610912292; _gid=GA1.2.381990959.1610912292; _fbp=fb.1.1610912292358.1831979940; u=2oiycodt.1oaavs8.dyu0a4x7fxw0; v=1610912321; buyer_laas_location=641780; buyer_location_id=641780; luri=novosibirsk; buyer_selected_search_radius4=0_general; buyer_local_priority_v2=0; sx=H4sIAAAAAAACAxXLQQqAIBAF0Lv8dYvRLEdvU0MIBU0iKCHePXr71zGfefd1W5RLYick2kSakiB2VETclpf85n19RJMSp4vJOSlM%2F2BMOBDNaigE9taM8QH0oydNVAAAAA%3D%3D; dfp_group=100; _ym_uid=1610912323905107257; _ym_d=1610912323; _ym_visorc_34241905=b; _ym_isad=2; _ym_visorc_419506=w; _ym_visorc_188382=w; __gads=ID=2cff056a4e50a953-22d0341a94b900a6:T=1610912323:S=ALNI_MZMbOe0285QjW7EVvsYtSa-RA_Vpg; f=5.8696cbce96d2947c36b4dd61b04726f1a816010d61a371dda816010d61a371dda816010d61a371dda816010d61a371ddbb0992c943830ce0bb0992c943830ce0bb0992c943830ce0a816010d61a371dd2668c76b1faaa358c08fe24d747f54dc0df103df0c26013a0df103df0c26013a2ebf3cb6fd35a0ac0df103df0c26013a8b1472fe2f9ba6b978e38434be2a23fac7b9c4258fe3658d831064c92d93c3903815369ae2d1a81d04dbcad294c152cb0df103df0c26013a20f3d16ad0b1c5462da10fb74cac1eab2da10fb74cac1eab3c02ea8f64acc0bdf0c77052689da50d2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab91e52da22a560f5503c77801b122405c48ab0bfc8423929a6d7a5083cc1669877def5708993e2ca678f1dc04f891d61e35b0929bad7c1ea5dec762b46b6afe81f200c638bc3d18ce60768b50dd5e12c30e37135e8f7c6b64dc9f90003c0354a346b8ae4e81acb9fa46b8ae4e81acb9fa02c68186b443a7acf8b817f3dc0c3f21c1eac53cc61955882da10fb74cac1eab2da10fb74cac1eab5e5aa47e7d07c0f95e1e792141febc9cb841da6c7dc79d0b' \
#############################
cookie = 'u=2tfvnhcb.ctv4iw.tymf98eh5pg0; _ym_d=1660584169; _ym_uid=166058416969271515; _gcl_au=1.1.56989214.1660584169; tmr_lvid=6bb642e099f3f60718329989304e0ddf; tmr_lvidTS=1660584170025; adrcid=Abu-CyKSxNnrOfCzX3o7WJw; buyer_laas_location=652000; uxs_uid=9f96c750-2309-11ed-a6ad-f34fafad57a6; buyer_location_id=652000; luri=rostov-na-donu; _gid=GA1.2.1638777385.1661600246; f=5.cc913c231fb04ced4b5abdd419952845a68643d4d8df96e9a68643d4d8df96e9a68643d4d8df96e9a68643d4d8df96e94f9572e6986d0c624f9572e6986d0c624f9572e6986d0c62ba029cd346349f36c1e8912fd5a48d02c1e8912fd5a48d0246b8ae4e81acb9fa143114829cf33ca746b8ae4e81acb9fa46b8ae4e81acb9fae992ad2cc54b8aa8b175a5db148b56e92157fc552fc06411bc8794f0f6ce82fe915ac1de0d034112dc0d86d9e44006d8143114829cf33ca7143114829cf33ca7c772035eab81f5e1fb0fb526bb39450a87829363e2d856a2b5b87f59517a23f2c772035eab81f5e13de19da9ed218fe23de19da9ed218fe2c772035eab81f5e1143114829cf33ca7172c80659da4d447f1cc8f457244b1a81ac794a8d120d7dc3fa8c565c3a4ea025cc116b628bd61b75d3d12014bda85a4087cf35ba7d977642e1c124e209506cf29aa4cecca288d6b767bc15421a53740cde1c78086b997c046b8ae4e81acb9fa46b8ae4e81acb9fa02c68186b443a7ac4c51f6e3637213638418bac8c3b019882da10fb74cac1eab2da10fb74cac1eabbe1b8fec550f290a09360354b9a5173a3778cee096b7b985bf37df0d1894b088; ft="24CG5tzXFLJmY1UjO4748/U5Wcmjkkpj5FkT7xo1OJOtPxazmZH4rWeEs53H+1m4zGnvXGHl1CG3Bmd7e5oe3VPMAgdQODpzZIXYsqzn4VVeI0PjJZgrr3/niuxjq49Lnjdw6Pf4xPbI6I6F8mC1JpbNVUms1vF9Vz5kj7DeX7tOHeBWSFgRv+VfOvBROhO6"; redirectMav=1; v=1661674970; dfp_group=38; _ym_visorc=b; _ym_isad=2; isCriteoSetNew=true; SEARCH_HISTORY_IDS=0%2C2%2C%2C4; sx=H4sIAAAAAAAC%2F1zRS67iMBBA0b1kzMC%2FqrLfbuwqO%2BSDQ4AkJE%2FsvcWAbtEbOLrS%2FW10KFSUiuAhglUlJbBFWBgVUCyu%2Bflt1uanKQuPotuzB9pwKQyZrnwM%2B%2BHmOvS1OTW5%2BdGImlCjpdepAa2MCTqD0jpp43ymVEwJkQXRGvORRRZn4elcTtOK47G5PDwEbunAeqD%2BJ2PQFv1bdhCVOM%2BmRIksmpOPtmRHpCjn%2BJGXspmB7q6fpjZ1bdwdVczd3HcHX0v71ewpvOWogkrRE2QOolViUYaigozFJs8fud7y0epxEM%2FPYzPVuKTjrtbpnla%2FTV%2Byo3czIiILYQkYAB2GTCnbIASKmSR8ZOpjGR5OXS4tLW7EutZl3ve6DcPTlfk%2F2b5OTUSvFTkqEoUyBLQ5hmTYKrLo2X7kKw28zABFXyzjuR7QcVs1VVplafdvOcDr1IgvBbNkZXSEzNYYCQgcnPJiWMrf5mmO3f0x2a2%2FPQFoefK5P9%2BXwfhuHMPXQRPo9foTAAD%2F%2FwJADIJ3AgAA; abp=0; _ga_9E363E7BES=GS1.1.1661674982.17.1.1661675492.60.0.0; buyer_from_page=catalog; _ga_M29JC28873=GS1.1.1661674982.17.1.1661675492.60.0.0; _ga=GA1.2.1813055663.1660584170; _dc_gtm_UA-2546784-1=1; _buzz_fpc=JTdCJTIycGF0aCUyMiUzQSUyMiUyRiUyMiUyQyUyMmRvbWFpbiUyMiUzQSUyMi53d3cuYXZpdG8ucnUlMjIlMkMlMjJleHBpcmVzJTIyJTNBJTIyTW9uJTJDJTIwMjglMjBBdWclMjAyMDIzJTIwMDglM0EzMSUzQTMyJTIwR01UJTIyJTJDJTIyU2FtZVNpdGUlMjIlM0ElMjJMYXglMjIlMkMlMjJ2YWx1ZSUyMiUzQSUyMiU3QiU1QyUyMnZhbHVlJTVDJTIyJTNBJTVDJTIyY2YzMDY3ZDU1MTc0NDRlZWRmNzMzNDgwZWQ2ZWNmYjglNUMlMjIlMkMlNUMlMjJmcGpzRm9ybWF0JTVDJTIyJTNBdHJ1ZSU3RCUyMiU3RA==; cto_bundle=2JKQZV93UlJZZW1obWZ3Tm1oQkolMkJNVVppZnRYaG95bzlzQ3FJVmIwOUZDdmxLaG4yVUNkam9WZXJmVWdNU05lYmZvRXZIc3N4ZnJhVnhlTDRzV2VXclg0TnFVNTklMkJvJTJCVzlzTkdhMjJyd0pkakQlMkYzbVFrciUyRnAlMkZCbWZSNGxtNVpBb2pDZG5JM1NyV3FNSCUyRnJuNyUyQmh5S3JzYTlRJTNEJTNE; tmr_reqNum=280; tmr_detect=0%7C1661675496313'
############################

# Если забанили, то добавьте свои куки, это не боевой код но он делает то, что надо
search = 'suzuki+gsx-r'     # Строка поиска на сайте и ниже параметры выбора города, радиуса разброса цены и т.п.
categoryId = 14
locationId = 641780         # Новосибирск
searchRadius = 200
priceMin = 200000
priceMax = 450000
sort = 'priceDesc'
withImagesOnly = 'true'     # Только с фото
limit_page = 50     # Количество объявлений на странице 50 максимум

def except_error(res): # Эту функцию можно дополнить, например обработку капчи
    print('ошибка')
    print(res.status_code, res.text)
    sys.exit(1)

s = requests.Session()                          # Будем всё делать в рамках одной сессии

#             'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Mobile Safari/537.36',
# Задаем заголовки:
headers = { 'authority': 'm.avito.ru',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'cookie': 'u=2tfvnhcb.ctv4iw.tymf98eh5pg0; _ym_d=1660584169; _ym_uid=166058416969271515; _gcl_au=1.1.56989214.1660584169; tmr_lvid=6bb642e099f3f60718329989304e0ddf; tmr_lvidTS=1660584170025; adrcid=Abu-CyKSxNnrOfCzX3o7WJw; buyer_laas_location=652000; uxs_uid=9f96c750-2309-11ed-a6ad-f34fafad57a6; buyer_location_id=652000; luri=rostov-na-donu; _gid=GA1.2.1638777385.1661600246; f=5.cc913c231fb04ced4b5abdd419952845a68643d4d8df96e9a68643d4d8df96e9a68643d4d8df96e9a68643d4d8df96e94f9572e6986d0c624f9572e6986d0c624f9572e6986d0c62ba029cd346349f36c1e8912fd5a48d02c1e8912fd5a48d0246b8ae4e81acb9fa143114829cf33ca746b8ae4e81acb9fa46b8ae4e81acb9fae992ad2cc54b8aa8b175a5db148b56e92157fc552fc06411bc8794f0f6ce82fe915ac1de0d034112dc0d86d9e44006d8143114829cf33ca7143114829cf33ca7c772035eab81f5e1fb0fb526bb39450a87829363e2d856a2b5b87f59517a23f2c772035eab81f5e13de19da9ed218fe23de19da9ed218fe2c772035eab81f5e1143114829cf33ca7172c80659da4d447f1cc8f457244b1a81ac794a8d120d7dc3fa8c565c3a4ea025cc116b628bd61b75d3d12014bda85a4087cf35ba7d977642e1c124e209506cf29aa4cecca288d6b767bc15421a53740cde1c78086b997c046b8ae4e81acb9fa46b8ae4e81acb9fa02c68186b443a7ac4c51f6e3637213638418bac8c3b019882da10fb74cac1eab2da10fb74cac1eabbe1b8fec550f290a09360354b9a5173a3778cee096b7b985bf37df0d1894b088; ft="24CG5tzXFLJmY1UjO4748/U5Wcmjkkpj5FkT7xo1OJOtPxazmZH4rWeEs53H+1m4zGnvXGHl1CG3Bmd7e5oe3VPMAgdQODpzZIXYsqzn4VVeI0PjJZgrr3/niuxjq49Lnjdw6Pf4xPbI6I6F8mC1JpbNVUms1vF9Vz5kj7DeX7tOHeBWSFgRv+VfOvBROhO6"; redirectMav=1; v=1661674970; dfp_group=38; _ym_visorc=b; _ym_isad=2; isCriteoSetNew=true; SEARCH_HISTORY_IDS=0%2C2%2C%2C4; sx=H4sIAAAAAAAC%2F1zRS67iMBBA0b1kzMC%2FqrLfbuwqO%2BSDQ4AkJE%2FsvcWAbtEbOLrS%2FW10KFSUiuAhglUlJbBFWBgVUCyu%2Bflt1uanKQuPotuzB9pwKQyZrnwM%2B%2BHmOvS1OTW5%2BdGImlCjpdepAa2MCTqD0jpp43ymVEwJkQXRGvORRRZn4elcTtOK47G5PDwEbunAeqD%2BJ2PQFv1bdhCVOM%2BmRIksmpOPtmRHpCjn%2BJGXspmB7q6fpjZ1bdwdVczd3HcHX0v71ewpvOWogkrRE2QOolViUYaigozFJs8fud7y0epxEM%2FPYzPVuKTjrtbpnla%2FTV%2Byo3czIiILYQkYAB2GTCnbIASKmSR8ZOpjGR5OXS4tLW7EutZl3ve6DcPTlfk%2F2b5OTUSvFTkqEoUyBLQ5hmTYKrLo2X7kKw28zABFXyzjuR7QcVs1VVplafdvOcDr1IgvBbNkZXSEzNYYCQgcnPJiWMrf5mmO3f0x2a2%2FPQFoefK5P9%2BXwfhuHMPXQRPo9foTAAD%2F%2FwJADIJ3AgAA; abp=0; _ga_9E363E7BES=GS1.1.1661674982.17.1.1661675492.60.0.0; buyer_from_page=catalog; _ga_M29JC28873=GS1.1.1661674982.17.1.1661675492.60.0.0; _ga=GA1.2.1813055663.1660584170; _dc_gtm_UA-2546784-1=1; _buzz_fpc=JTdCJTIycGF0aCUyMiUzQSUyMiUyRiUyMiUyQyUyMmRvbWFpbiUyMiUzQSUyMi53d3cuYXZpdG8ucnUlMjIlMkMlMjJleHBpcmVzJTIyJTNBJTIyTW9uJTJDJTIwMjglMjBBdWclMjAyMDIzJTIwMDglM0EzMSUzQTMyJTIwR01UJTIyJTJDJTIyU2FtZVNpdGUlMjIlM0ElMjJMYXglMjIlMkMlMjJ2YWx1ZSUyMiUzQSUyMiU3QiU1QyUyMnZhbHVlJTVDJTIyJTNBJTVDJTIyY2YzMDY3ZDU1MTc0NDRlZWRmNzMzNDgwZWQ2ZWNmYjglNUMlMjIlMkMlNUMlMjJmcGpzRm9ybWF0JTVDJTIyJTNBdHJ1ZSU3RCUyMiU3RA==; cto_bundle=2JKQZV93UlJZZW1obWZ3Tm1oQkolMkJNVVppZnRYaG95bzlzQ3FJVmIwOUZDdmxLaG4yVUNkam9WZXJmVWdNU05lYmZvRXZIc3N4ZnJhVnhlTDRzV2VXclg0TnFVNTklMkJvJTJCVzlzTkdhMjJyd0pkakQlMkYzbVFrciUyRnAlMkZCbWZSNGxtNVpBb2pDZG5JM1NyV3FNSCUyRnJuNyUyQmh5S3JzYTlRJTNEJTNE; tmr_reqNum=280; tmr_detect=0%7C1661675496313',
            'sec-fetch-site': 'none',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'accept-language': 'ru-RU,ru;q=0.9',}
###############################################################################
# headers = { 'authority': 'www.m.avito.ru',
#         :scheme: https
#         accept: */*
#         accept-encoding: gzip, deflate, br
#         accept-language: en-US,en;q=0.9,ru;q=0.8
#         content-length: 988
#         content-type: application/json; charset=UTF-8
#         cookie: u=2tfvnhcb.ctv4iw.tymf98eh5pg0; _ym_d=1660584169; _ym_uid=166058416969271515; _gcl_au=1.1.56989214.1660584169; tmr_lvid=6bb642e099f3f60718329989304e0ddf; tmr_lvidTS=1660584170025; adrcid=Abu-CyKSxNnrOfCzX3o7WJw; buyer_laas_location=652000; uxs_uid=9f96c750-2309-11ed-a6ad-f34fafad57a6; buyer_location_id=652000; luri=rostov-na-donu; _gid=GA1.2.1638777385.1661600246; f=5.cc913c231fb04ced4b5abdd419952845a68643d4d8df96e9a68643d4d8df96e9a68643d4d8df96e9a68643d4d8df96e94f9572e6986d0c624f9572e6986d0c624f9572e6986d0c62ba029cd346349f36c1e8912fd5a48d02c1e8912fd5a48d0246b8ae4e81acb9fa143114829cf33ca746b8ae4e81acb9fa46b8ae4e81acb9fae992ad2cc54b8aa8b175a5db148b56e92157fc552fc06411bc8794f0f6ce82fe915ac1de0d034112dc0d86d9e44006d8143114829cf33ca7143114829cf33ca7c772035eab81f5e1fb0fb526bb39450a87829363e2d856a2b5b87f59517a23f2c772035eab81f5e13de19da9ed218fe23de19da9ed218fe2c772035eab81f5e1143114829cf33ca7172c80659da4d447f1cc8f457244b1a81ac794a8d120d7dc3fa8c565c3a4ea025cc116b628bd61b75d3d12014bda85a4087cf35ba7d977642e1c124e209506cf29aa4cecca288d6b767bc15421a53740cde1c78086b997c046b8ae4e81acb9fa46b8ae4e81acb9fa02c68186b443a7ac4c51f6e3637213638418bac8c3b019882da10fb74cac1eab2da10fb74cac1eabbe1b8fec550f290a09360354b9a5173a3778cee096b7b985bf37df0d1894b088; ft="24CG5tzXFLJmY1UjO4748/U5Wcmjkkpj5FkT7xo1OJOtPxazmZH4rWeEs53H+1m4zGnvXGHl1CG3Bmd7e5oe3VPMAgdQODpzZIXYsqzn4VVeI0PjJZgrr3/niuxjq49Lnjdw6Pf4xPbI6I6F8mC1JpbNVUms1vF9Vz5kj7DeX7tOHeBWSFgRv+VfOvBROhO6"; redirectMav=1; v=1661674970; dfp_group=38; _ym_visorc=b; _ym_isad=2; isCriteoSetNew=true; SEARCH_HISTORY_IDS=0%2C2%2C%2C4; sx=H4sIAAAAAAAC%2F1zRS67iMBBA0b1kzMC%2FqrLfbuwqO%2BSDQ4AkJE%2FsvcWAbtEbOLrS%2FW10KFSUiuAhglUlJbBFWBgVUCyu%2Bflt1uanKQuPotuzB9pwKQyZrnwM%2B%2BHmOvS1OTW5%2BdGImlCjpdepAa2MCTqD0jpp43ymVEwJkQXRGvORRRZn4elcTtOK47G5PDwEbunAeqD%2BJ2PQFv1bdhCVOM%2BmRIksmpOPtmRHpCjn%2BJGXspmB7q6fpjZ1bdwdVczd3HcHX0v71ewpvOWogkrRE2QOolViUYaigozFJs8fud7y0epxEM%2FPYzPVuKTjrtbpnla%2FTV%2Byo3czIiILYQkYAB2GTCnbIASKmSR8ZOpjGR5OXS4tLW7EutZl3ve6DcPTlfk%2F2b5OTUSvFTkqEoUyBLQ5hmTYKrLo2X7kKw28zABFXyzjuR7QcVs1VVplafdvOcDr1IgvBbNkZXSEzNYYCQgcnPJiWMrf5mmO3f0x2a2%2FPQFoefK5P9%2BXwfhuHMPXQRPo9foTAAD%2F%2FwJADIJ3AgAA; abp=0; _ga_9E363E7BES=GS1.1.1661674982.17.1.1661675492.60.0.0; buyer_from_page=catalog; _ga_M29JC28873=GS1.1.1661674982.17.1.1661675492.60.0.0; _ga=GA1.2.1813055663.1660584170; _dc_gtm_UA-2546784-1=1; _buzz_fpc=JTdCJTIycGF0aCUyMiUzQSUyMiUyRiUyMiUyQyUyMmRvbWFpbiUyMiUzQSUyMi53d3cuYXZpdG8ucnUlMjIlMkMlMjJleHBpcmVzJTIyJTNBJTIyTW9uJTJDJTIwMjglMjBBdWclMjAyMDIzJTIwMDglM0EzMSUzQTMyJTIwR01UJTIyJTJDJTIyU2FtZVNpdGUlMjIlM0ElMjJMYXglMjIlMkMlMjJ2YWx1ZSUyMiUzQSUyMiU3QiU1QyUyMnZhbHVlJTVDJTIyJTNBJTVDJTIyY2YzMDY3ZDU1MTc0NDRlZWRmNzMzNDgwZWQ2ZWNmYjglNUMlMjIlMkMlNUMlMjJmcGpzRm9ybWF0JTVDJTIyJTNBdHJ1ZSU3RCUyMiU3RA==; cto_bundle=2JKQZV93UlJZZW1obWZ3Tm1oQkolMkJNVVppZnRYaG95bzlzQ3FJVmIwOUZDdmxLaG4yVUNkam9WZXJmVWdNU05lYmZvRXZIc3N4ZnJhVnhlTDRzV2VXclg0TnFVNTklMkJvJTJCVzlzTkdhMjJyd0pkakQlMkYzbVFrciUyRnAlMkZCbWZSNGxtNVpBb2pDZG5JM1NyV3FNSCUyRnJuNyUyQmh5S3JzYTlRJTNEJTNE; tmr_reqNum=280; tmr_detect=0%7C1661675496313
#         origin: https://www.avito.ru
#         referer: https://www.avito.ru/rostov-na-donu/kvartiry
#         sec-ch-ua: "Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"
#         sec-ch-ua-mobile: ?1
#         sec-ch-ua-platform: "Android"
#         sec-fetch-dest: empty
#         sec-fetch-mode: cors
#         sec-fetch-site: same-origin
#         user-agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36
#         x-requested-with: XMLHttpRequest
##############################################################################

# if cookie:                                      # Добавим куки, если есть внешние куки
#     headers['cookie'] = cookie
s.headers.update(headers)                       # Сохраняем заголовки в сессию
s.get('https://m.avito.ru/')                    # Делаем запрос на мобильную версию.
url_api_9 = 'https://m.avito.ru/api/9/items'    # Урл первого API, позволяет получить id и url объявлений по заданным фильтрам
                                                # Тут уже видно цену и название объявлений
params = {
    'categoryId': 14,
    'params[30]': 4969,
    'locationId': locationId,
    'searchRadius': searchRadius,
    'priceMin': priceMin,
    'priceMax': priceMax,
    'params[110275]': 426645,
    'sort': sort,
    'withImagesOnly': withImagesOnly,
    'lastStamp': 1610905380,
    'display': 'list',
    'limit': limit_page,
    'query': search,
}
cicle_stop = True       # Переменная для остановки цикла
cikle = 0               # Переменная для перебора страниц с объявлениями
items = []              # Список, куда складываем объявления
params['key'] =  key
while cicle_stop:
    cikle += 1          # Так как страницы начинаются с 1, то сразу же итерируем
    params['page'] = cikle
    res = s.get(url_api_9, params=params)
    try:
        res = res.json()
    except json.decoder.JSONDecodeError:
        except_error(res)
    if res['status'] != 'ok':
            print(res['result'])
            sys.exit(1)
    if res['status'] == 'ok':
        items_page = int(len(res['result']['items']))

        if items_page > limit_page: # проверка на "snippet"
            items_page = items_page - 1

        for item in res['result']['items']:
            if item['type'] == 'item':
                items.append(item)
        if items_page < limit_page:
            cicle_stop = False
####################################################################
params = {'key': key}
for i in items: # Теперь идем по ябъявлениям:
    ad_id = str(i['value']['id'])
    # url_more_data_1 = 'https://m.avito.ru/api/1/rmp/show/' + ad_id  # more_data_1 = s.get(url_more_data_1, params=params).json() # Тут тоже моного информации, можете посмотреть
    url_more_data_2 = 'https://m.avito.ru/api/15/items/' + ad_id
    more_data_2 = s.get(url_more_data_2, params=params).json()
    if not 'error' in more_data_2:
        # print(more_data_2)            # В more_data_2 есть всё, что надо, я вывел на принт наиболее интересные для наглядности:
        print(more_data_2['title'])
        print(more_data_2['price'])
        print(more_data_2['address'])
        url_get_phone = 'https://m.avito.ru/api/1/items/' + ad_id + '/phone'    # URL для получения телефона
        phone = s.get(url_get_phone, params=params).json()                      # Сам запрос
        if phone['status'] == 'ok': phone_number = requests.utils.unquote(phone['result']['action']['uri'].split('number=')[1]) # Прверка на наличие телефона, такой странный синтсксис, чтоб уместиться в 100 сторочек кода)))
        else: phone_number = phone['result']['message']
        print(phone_number)
        print(more_data_2['seller'])
        # print(more_data_2['description']) # Скрыл, т.к. много букв
        print('=======================================================\n')