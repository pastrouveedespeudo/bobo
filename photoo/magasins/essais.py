import requests
from bs4 import BeautifulSoup

url = "https://www.google.com/search?ei=Gnn5XJP5KIu5gweW1qaQBQ&q=Coiffure%20Marilyne+crest+horraires&oq=Coiffure%20Marilyne+crest+horraires"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
tb = soup.find_all('div')

print(tb)
