from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.imdb.com/list/ls096735829/?sort=moviemeter,asc&st_dt=&mode=detail&page=1"

page = urlopen(url)

html = page.read().decode("utf-8")

soup = BeautifulSoup(html, "html.parser")

# print(soup.get_text())

#News = soup.find_all("")


# print(News)
# main body of web page
content = soup.find(id="main")


# title of article
articleTitle = soup.find("h1", class_="header").text.replace("\n", "")

# copy the movie frame from article
#articleList = content.find_all("div", class_="article listo")
movie_frame = content.find_all("div", class_="lister-item mode-detail")

# show 1 -10 moviews first line in article
for i in range(0, 42):
    movie_first_line = movie_frame[i].find("h3", class_="lister-item-header")
    # show movie title
    movieTitle = movie_first_line.find("a").text
    print(movieTitle)


# <a href="/title/tt10310140/?ref_=ttls_li_tt">Fatman</a>
# <a href="/title/tt7737786/?ref_=ttls_li_tt">Greenland</a>
