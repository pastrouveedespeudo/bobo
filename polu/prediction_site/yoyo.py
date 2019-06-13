import os
import cv2
import json
import requests
import datetime
import urllib.request
from bs4 import *
from colour import Color
from PIL import Image, ImageDraw, ImageChops

date = datetime.datetime.now()

jour = date.day
mois = date.month
année = date.year

heure = date.hour
minute = date.minute


jour = ['samedi', 'dimanche']


date = datetime.datetime.now()

heure = date.hour
jour = date.weekday()

print(jour)

if jour == 5 or jour == 6:
    pass
else:
    pass










