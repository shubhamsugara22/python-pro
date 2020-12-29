# program  to scrape top 100 movies in IMDB with their ratings
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.imdb.com/list/ls096735829/?sort=moviemeter,asc&st_dt=&mode=detail&page=1"
url1 = "https://www.imdb.com/list/ls096735829/?sort=moviemeter,asc&st_dt=&mode=detail&page=2"

page = urlopen(url)
page1 = urlopen(url1)

html = page.read().decode("utf-8")
html1 = page.read().decode("utf-8")

soup = BeautifulSoup(html, "html.parser")
soup1 = BeautifulSoup(html1, "html.parser")
# print(soup.get_text())

#News = soup.find_all("")


# print(News)
# main body of web page
content = soup.find(id="main")

page2 = soup.find(id="main")

# title of article
articleTitle = soup.find("h1", class_="header").text.replace("\n", "")
print(articleTitle)

# copy the movie frame from article
#articleList = content.find_all("div", class_="article listo")
movie_frame = content.find_all("div", class_="lister-item mode-detail")

movie_frame1 = page2.find_all("div", class_="lister-item mode-detail")


titles_of_movies = []
# show 1 -10 moviews first line in article
for i in range(0, 42):
    movie_first_line = movie_frame[i].find("h3", class_="lister-item-header")
    # show movie title
    movieTitle = movie_first_line.find("a").text
    movie_rating = movie_frame[i].find(
        "span", class_="ipl-rating-star__rating").text
    print(movieTitle, movie_rating)
    titles_of_movies.append(movieTitle)
    # print(movieTitle)

# for i in range(0, 10):
#     movie_line = movie_frame1[i].find("h3", class_="lister-item-header")
#     movieTitle1 = movie_line.find("a").text
#     titles_of_movies.append(movieTitle1)
#     print(movieTitle1)

print(titles_of_movies)
# <a href="/title/tt10310140/?ref_=ttls_li_tt">Fatman</a>
# <a href="/title/tt7737786/?ref_=ttls_li_tt">Greenland</a>
