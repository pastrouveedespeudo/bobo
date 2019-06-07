from bs4 import BeautifulSoup
import requests
metacriticaddress = "http://www.metacritic.com/search/tv/game%20of%20thrones/results"
r = requests.get(metacriticaddress, headers={
     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36"
 })
soup = BeautifulSoup(r.content, "html.parser")
first_result = soup.find_all("li", class_="first_result")
print(first_result)
