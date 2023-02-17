

#категории + нас. пункт id + URL PATH
#https://m.avito.ru/api/2/search/main?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&locationId=652120

#НЕТ В общем запрсе ID & PATH НЕТУ!
#! В HTML карточке объявления путь к ID City
#https://www.avito.ru/bryansk/zapchasti_i_aksessuary/dvigatel_na_skuter_150_kubov_157qmj_2332435829
    #//*[@id="app"]/div/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[2]/div/div[3]
    #XPATH = .//div//div//div[@data-map-type='dynamic']
    #<div class="style-item-map-wrapper-ElFsX" data-map-zoom="16"
    # data-map-lat="53.233451" data-map-lon="34.358116" data-map-type="dynamic"

    # data-item-id="2332435829" ID объявления
    # data-location-id="623880" ID City
    # data-category-id="10" ID Kategory

#API/9 JSON Смотрим после "items"
#    "seoNavigation": {
#       "breadcrumbs": [
#         {
#           "name": "Лабинск",
#           "title": "Все объявления в Лабинске",
#           "url": "/labinsk"
#         },
#         {
#           "name": "Транспорт",
#           "title": "Транспорт в Лабинске",
#           "url": "/labinsk/transport"
#         },
#         {
#           "name": "Автомобили",
#           "title": "Автомобили в Лабинске",
#           "url": "/labinsk/avtomobili"
#         }
#       ]
#     },

#file:///C:/Users/miladmin/Downloads/%D0%9F%D0%B0%D1%80%D1%81%D0%B8%D0%BD%D0%B3/%D0%9F%D0%B0%D1%80%D1%81%20%D0%9A%D0%B0%D1%82%D0%B0%D0%BB%D0%BE%D0%B3%20%D0%B0%D0%B2%D1%82%D0%BE%D0%BC%D0%BE%D0%B1%D0%B8%D0%BB%D0%B5%D0%B9%20_%20%D0%90%D0%B2%D0%B8%D1%82%D0%BE.mhtml
#//*[@id="app"]/div/div[2]/div[2]/span/div
#//*[@id="app"]/div/div[2]/div[2]/span  //div[@data-marker="more-popup"]
#//*[@id="app"]/div//div[@data-marker="more-popup"] //a[substring(@class,1,9) ="link-link"]
#//*[@id="app"]/div//div[@data-marker="more-popup"] //a[substring(@class,1,9) ="link-link"]//
#////*[@id="app"]/div//div[@data-marker="more-popup"] //a[substring(@class,1,9) ="link-link"]//text()




