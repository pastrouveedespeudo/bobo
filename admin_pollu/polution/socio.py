import os
import cv2
import json
import pyglet
import requests
import datetime
import urllib.request
from bs4 import *
from colour import Color
from PIL import Image, ImageDraw, ImageChops






def habitant(lieu, POPULATION_ACTIVE_HABITANT):


    lyon = 328469
    paris = 1350800 
    marseille = 762480 

    if lieu == 'lyon':
        POPULATION_ACTIVE_HABITANT['supp300K'] += 1

    if lieu == 'paris':
        POPULATION_ACTIVE_HABITANT['sup1M'] += 1

    if lieu == 'marseille':
        POPULATION_ACTIVE_HABITANT['sup500K'] += 1
    #population active de 15 a 59 ans














