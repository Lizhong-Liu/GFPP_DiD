#!/usr/bin/env python

from bs4 import BeautifulSoup as bs
import requests

# Children Health Status - From LA Health Department
addr = "http://www.publichealth.lacounty.gov/ha/HA_DATA_TRENDS.htm#Child"
resp = requests.get(addr)
html = resp.content
soup = bs(html, "html.parser")
links = [i.get("href") for i in soup.find_all("a") if ".xls" in str(i.get("href"))]
docs = [i for i in links if "Child" in str(i)]

downloads = [i for i in docs if "Health" in i or "Routines" in i or "Behaviors" in i or "Food" in i]
for i in downloads:
    if "http" not in str(i):
        downloads.remove(i)

for i in downloads[1:-7]:
    resp = requests.get(i)
    file_name = "{}".format(i.split("/")[-1])
    with open("health/{}".format(file_name), "wb") as out:
        out.write(resp.content)

# School enrollment
addr = "https://www.cde.ca.gov/ds/sd/sd/filesenr.asp"
resp = requests.get(addr)
html = resp.content
soup = bs(html, "html.parser")

td = [i for i in soup.find_all("td")]
enr = []
for i in td:
    l = i.find("a")
    if l != None:
        link = l.get("href")
        enr.append(link)
enr = [enr[i] for i in range(0,len(enr),2)][:16]

for i in enr[0]:
    if i == "Y":
        print(enr[0].index(i))

datas = []
for i in enr:
    resp = requests.get(i)
    file_name = "{}.txt".format(i[70:74])
    datas.append(file_name)
    with open("data/{}".format(file_name), "w") as out:
        out.write(resp.text)
