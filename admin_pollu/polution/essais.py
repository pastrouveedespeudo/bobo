import requests
import cv2
from PIL import Image

clé = '5a72ceae1feda40543d5844b2e04a205'
lieu = 'lyon'
localisation = "http://api.openweathermap.org/data/2.5/weather?q={0},fr&appid={1}".format(lieu,clé)
r = requests.get(localisation)
data=r.json()

print(data)
