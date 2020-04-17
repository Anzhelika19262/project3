# import rsa
#
# mess = 'Hello, Codeby!'
# (pubkey, privkey) = rsa.newkeys(600) # Генерируем 2 ключа
# print(privkey, pubkey)
# cipher = rsa.encrypt(mess.encode("utf-8"), pubkey) # Шифруем
# print(cipher)
# mess = rsa.decrypt(cipher, privkey) # Расшифровываем
# print(mess)
import os
from io import BytesIO
#
# import requests
from PIL import Image
#
#
# map_api_server = 'https://static-maps.yandex.ru/1.x/?ll=38.841371%2C45.775550&z=1&size=650,450&l=map'
#
# response = requests.get(map_api_server)
# if not response:
#     pass
# Image.open(BytesIO(
#     response.content)).show()
# import requests
# api_server = "http://static-maps.yandex.ru/1.x/"
# params = {
#     "ll": "38.841371,45.775550",
#     "l": "map",
#     'z': '1',
#     'size': '650,400'
# }
# response = requests.get(api_server, params=params)
# map_file = 'map_img/map.png'
# with open(map_file, "wb") as file:
#     file.write(response.content)
import requests
toponym_to_find = input()
geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": toponym_to_find,
    "format": "json"}
response = requests.get(geocoder_api_server, params=geocoder_params)
if not response:
    print('No')
json_response = response.json()
toponym_coodrinates = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
print(toponym_coodrinates)