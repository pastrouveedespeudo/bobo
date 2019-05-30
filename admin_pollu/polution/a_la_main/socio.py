import os
import cv2
import json
import requests
import datetime
import urllib.request
from bs4 import *
from colour import Color
from PIL import Image, ImageDraw, ImageChops






def habitant(lieu):


    lyon = 328469
    paris = 1350800 
    marseille = 762480 

    if lieu == 'lyon':
        return 'supp300K'

    if lieu == 'paris':
        return 'sup1M'

    if lieu == 'marseille':
        return 'sup500K'
    #population active de 15 a 59 ans














