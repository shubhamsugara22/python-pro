import numpy as np
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup


url = "https://towardsdatascience.com/top-10-in-demand-web-development-frameworks-in-2021-8a5b668be0d6"

page = urlopen(url).read()

html = page.read().decode("utf-8")

soup = BeautifulSoup(html, "html-parser")

content = soup.find(id="main")
print(content)
