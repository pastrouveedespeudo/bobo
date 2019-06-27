"""Here for the site web we document variables"""
import requests
import datetime
import urllib.request
from bs4 import *



def habitant(lieu):
    """We define variables"""
    
    lyon = 328469
    paris = 1350800 
    marseille = 762480 

    if lieu == 'lyon':
        return 'supp300K'

    if lieu == 'paris':
        return 'sup1M'

    if lieu == 'marseille':
        return 'sup500K'















