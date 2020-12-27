from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.imdb.com/list/ls096735829/?sort=moviemeter,asc&st_dt=&mode=detail&page=1"

page = urlopen(url)

html = page.read().decode("utf-8")

soup = BeautifulSoup(html, "html.parser")

print(soup.get_text())
