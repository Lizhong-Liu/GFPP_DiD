# fetch physical fitness data
import pandas as pd
import requests, zipfile, io
from bs4 import BeautifulSoup as bs
resp = requests.get("https://www.cde.ca.gov/ta/tg/pf/pftresearch.asp")
soup = bs(resp.content, "html.parser")
rows = soup.find("table").find_all('td')[1:]
rows = [x for x in rows if ("div" in str(x)) or ("a" in str(x))]
links = {}
for i in range(0,len(rows),2):
    links[str(rows[i].text)] = rows[i+1].find("a").get("href")

for x in links.values():
    year = list(links.keys())[list(links.values()).index(x)]
    response = requests.get(x)
    zipDocument = zipfile.ZipFile(io.BytesIO(response.content))
    zipDocument.extractall('PTF_{}'.format(year))
