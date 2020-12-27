import re
from urllib.request import urlopen


url = "https://www.imdb.com/list/ls096735829/?sort=moviemeter,asc&st_dt=&mode=detail&page=1"

page = urlopen(url)

html_bytes = page.read()

html = html_bytes.decode("utf-8")

# print(html)


pattern = "<title.*?>.*?</title.*?>"

match_result = re.search(pattern, html, re.IGNORECASE)

title = match_result.group()

title = re.sub("<.*?>", "", title)

print(title)
